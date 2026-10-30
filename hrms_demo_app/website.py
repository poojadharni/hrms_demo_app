def resolve_path(path):
	if path.strip("/") == "login":
		return "hrms_login"

	return path


def get_website_user_home_page(user):
	"""Serve the Vue HRMS Portal landing page (`www/index.html`) at `/`."""
	return "index"