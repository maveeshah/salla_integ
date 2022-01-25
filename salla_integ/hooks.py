from . import __version__ as app_version

app_name = "salla_integ"
app_title = "Salla Integrations"
app_publisher = "Home"
app_description = "Integrate O & C"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hcbdshb@bjhk"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/salla_integ/css/salla_integ.css"
# app_include_js = "/assets/salla_integ/js/salla_integ.js"

# include js, css files in header of web template
# web_include_css = "/assets/salla_integ/css/salla_integ.css"
# web_include_js = "/assets/salla_integ/js/salla_integ.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "salla_integ/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "salla_integ.install.before_install"
# after_install = "salla_integ.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "salla_integ.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events


doc_events = {
	"*": {
		"after_insert": [
			"frappe.event_streaming.doctype.event_update_log.event_update_log.notify_consumers"
		],
		"on_update": [
			"frappe.desk.notifications.clear_doctype_notifications",
			"frappe.core.doctype.activity_log.feed.update_feed",
			"frappe.workflow.doctype.workflow_action.workflow_action.process_workflow_actions",
			"frappe.automation.doctype.assignment_rule.assignment_rule.apply",
			"frappe.core.doctype.file.file.attach_files_to_document",
			"frappe.event_streaming.doctype.event_update_log.event_update_log.notify_consumers",
			"frappe.automation.doctype.assignment_rule.assignment_rule.update_due_date",
			"frappe.core.doctype.user_type.user_type.apply_permissions_for_non_standard_user_type"
		],
		"after_rename": "frappe.desk.notifications.clear_doctype_notifications",
		"on_cancel": [
			"frappe.desk.notifications.clear_doctype_notifications",
			"frappe.workflow.doctype.workflow_action.workflow_action.process_workflow_actions"
		],
		"on_trash": [
			"frappe.desk.notifications.clear_doctype_notifications",
			"frappe.workflow.doctype.workflow_action.workflow_action.process_workflow_actions",
			"frappe.event_streaming.doctype.event_update_log.event_update_log.notify_consumers"
		],
		"on_update_after_submit": [
			"frappe.workflow.doctype.workflow_action.workflow_action.process_workflow_actions"
		],
		"on_change": [
			"frappe.social.doctype.energy_point_rule.energy_point_rule.process_energy_points",
			"frappe.automation.doctype.milestone_tracker.milestone_tracker.evaluate_milestone"
		]
	},
	"Event": {
		"after_insert": "frappe.integrations.doctype.google_calendar.google_calendar.insert_event_in_google_calendar",
		"on_update": "frappe.integrations.doctype.google_calendar.google_calendar.update_event_in_google_calendar",
		"on_trash": "frappe.integrations.doctype.google_calendar.google_calendar.delete_event_from_google_calendar",
	},
	"Contact": {
		"after_insert": "frappe.integrations.doctype.google_contacts.google_contacts.insert_contacts_to_google_contacts",
		"on_update": "frappe.integrations.doctype.google_contacts.google_contacts.update_contacts_to_google_contacts",
	},
	"DocType": {
		"after_insert": "frappe.cache_manager.build_domain_restriced_doctype_cache",
		"after_save": "frappe.cache_manager.build_domain_restriced_doctype_cache",
	},
	"Page": {
		"after_insert": "frappe.cache_manager.build_domain_restriced_page_cache",
		"after_save": "frappe.cache_manager.build_domain_restriced_page_cache",
	}
}


# Scheduled Tasks
# ---------------

scheduler_events = {
	"cron": {
		"*/5 * * * *": [
			"salla_integ.salla_integrations.api.get_customers",
			"salla_integ.salla_integrations.api.get_orders"
		]
	}

# 	"all": [
# 		"salla_integ.tasks.all"
# 	],
# 	"daily": [
# 		"salla_integ.tasks.daily"
# 	],
# 	"hourly": [
# 		"salla_integ.tasks.hourly"
# 	],
# 	"weekly": [
# 		"salla_integ.tasks.weekly"
# 	]
# 	"monthly": [
# 		"salla_integ.tasks.monthly"
# 	],
}

# Testing
# -------

# before_tests = "salla_integ.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "salla_integ.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "salla_integ.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"salla_integ.auth.validate"
# ]

