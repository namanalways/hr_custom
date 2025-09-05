import frappe

def before_save_investment_detail(doc, method=None):
    doc.custom_employee_investment_details = []
    for emp in doc.employees:
        investments = frappe.db.get_list("Employee Investment Declaration", filters={"employee": emp.employee})
        if investments:
            for investment in investments:
                print(investment)
                doc.append("custom_employee_investment_details", {
                    "id": investment.name,
                })