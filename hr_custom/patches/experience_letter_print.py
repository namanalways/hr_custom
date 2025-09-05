import frappe

def on_update_employee(doc, method=None):
    if doc.workflow_state == "Exit":
        pdf = frappe.get_print("Employee", doc.name, print_format="Experience Letter", as_pdf=True)
        file = frappe.get_doc({
            "doctype": "File",
            "file_name": f"Experience_Letter_{doc.employee_name}.pdf",
            "attached_to_doctype": "Employee",
            "attached_to_name": doc.name,
            "content": pdf,
            "is_private": 1
        })
        file.save()