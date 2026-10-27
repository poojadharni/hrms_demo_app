import ipaddress
from urllib.parse import urlsplit

import frappe
from frappe import _
from frappe.auth import LoginManager
from frappe.rate_limiter import rate_limit
from frappe.twofactor import should_run_2fa


def get_hrms_demo_users():
	website_context = frappe.local.conf.get("website_context") or {}
	demo_users = website_context.get("hrms_demo_users") or {}

	if not isinstance(demo_users, dict):
		raise TypeError("website_context.hrms_demo_users must be a dictionary")

	return {
		role: account.get("username", "") if isinstance(account, dict) else account or ""
		for role, account in demo_users.items()
	}


@frappe.whitelist(allow_guest=True, methods=["POST"])
@rate_limit(limit=10, seconds=300, methods=["POST"])
def quick_demo_login(role: str):
	if not frappe.conf.get("developer_mode"):
		frappe.throw(_("Demo quick login is available only in developer mode."), frappe.PermissionError)

	if frappe.get_request_header("X-Forwarded-For"):
		frappe.throw(_("Demo quick login is available only from a local connection."), frappe.PermissionError)

	origin = frappe.get_request_header("Origin")
	expected_origin = f"{frappe.request.scheme}://{frappe.request.host}"
	if not origin or urlsplit(origin).netloc != frappe.request.host or origin != expected_origin:
		frappe.throw(_("Demo quick login requires a same-origin request."), frappe.PermissionError)

	remote_addr = getattr(frappe.request, "remote_addr", None)
	try:
		is_local_request = remote_addr and ipaddress.ip_address(remote_addr).is_loopback
	except ValueError:
		is_local_request = False

	if not is_local_request:
		frappe.throw(_("Demo quick login is available only from a local connection."), frappe.PermissionError)

	if role not in {"admin", "employee", "hr"}:
		frappe.throw(_("Invalid demo account role."), frappe.ValidationError)

	website_context = frappe.local.conf.get("website_context") or {}
	demo_users = website_context.get("hrms_demo_users") or {}
	account = demo_users.get(role) if isinstance(demo_users, dict) else None
	if not isinstance(account, dict):
		frappe.throw(_("Demo credentials are not configured for this account."), frappe.ValidationError)

	username = account.get("username")
	password = account.get("password")
	if not username or not password:
		frappe.throw(_("Demo credentials are not configured for this account."), frappe.ValidationError)

	if role == "employee" and username.lower() == "administrator":
		frappe.throw(_("The Employee demo account must be a separate user."), frappe.ValidationError)

	if role == "hr" and username.lower() == "administrator":
		frappe.throw(_("The HR demo account must be a separate user."), frappe.ValidationError)

	if frappe.get_system_settings("disable_user_pass_login"):
		frappe.throw(_("Login with username and password is disabled."), frappe.AuthenticationError)

	login_manager = frappe.local.login_manager
	login_manager.run_trigger("before_login")
	login_manager.authenticate(user=username, pwd=password)

	roles = frappe.get_roles(login_manager.user)
	if role == "admin" and login_manager.user != "Administrator" and "System Manager" not in roles:
		frappe.throw(_("The Admin demo account must have System Manager access."), frappe.PermissionError)

	if role == "employee" and (
		login_manager.user == "Administrator"
		or "System Manager" in roles
		or not {"Employee", "Employee Self Service"}.intersection(roles)
	):
		frappe.throw(
			_("The Employee demo account must have Employee permissions and must not be an administrator."),
			frappe.PermissionError,
		)

	if role == "hr" and (
		login_manager.user == "Administrator"
		or "System Manager" in roles
		or "HR Manager" not in roles
	):
		frappe.throw(
			_("The HR demo account must have HR Manager access and must not be an administrator."),
			frappe.PermissionError,
		)

	if should_run_2fa(login_manager.user):
		frappe.throw(_("Demo quick login is unavailable for accounts with two-factor authentication."), frappe.PermissionError)

	if login_manager.force_user_to_reset_password():
		frappe.throw(_("This account must reset its password before demo login."), frappe.AuthenticationError)

	login_manager.post_login()
	frappe.local.response["home_page"] = "/desk"
