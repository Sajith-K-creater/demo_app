import frappe

def get_context(context):
    context.data=frappe.session.user
    return context