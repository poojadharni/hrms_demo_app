import frappe


def get_context(context):
	# `{{ csrf_token }}` is not part of the default website Jinja context;
	# provide it so the Vue bundle's `window.csrf_token` assignment works.
	context.csrf_token = frappe.sessions.get_csrf_token()
	# The rendered HTML embeds the session's CSRF token, so it must not be
	# served from Frappe's per-path website HTML cache.
	context.no_cache = 1
