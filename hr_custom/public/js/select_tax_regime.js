frappe.ui.form.on("Salary Structure Assignment", {
    employee: function(frm) {
        if (frm.doc.employee) {
            frappe.db.get_value("Employee", frm.doc.employee, "custom_tax_regime_preference")
                .then(r => {
                    if (r.message) {
                        let regime = r.message.custom_tax_regime_preference;
                        frm.set_value("salary_structure", regime);
                    }
                });
        }
    }
});