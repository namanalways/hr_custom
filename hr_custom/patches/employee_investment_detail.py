import frappe

def before_save_investment_detail(doc, method=None):
    for emp in doc.employees:
        doc.custom_employee_investment_details = []
        investments = frappe.db.get_list("Employee Investment Declaration", filters={"employee": emp.employee})
        if investments:
            for investment in investments:
                doc.append("custom_employee_investment_details", {
                    "id": investment.name,
                })