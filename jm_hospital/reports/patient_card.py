from odoo import api, models, _


# How To Call A Python Function While Printing PDF Report in Odoo
# https://www.youtube.com/watch?v=JGWc1KjyIBk&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=62
class PatientCardReport(models.AbstractModel):
    # mandatory name : report.modulename.reportname
    _name = 'report.jm_hospital.report_patient'
    _description = 'Patient card Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # docid --> id of the record (here patient_id
        print(docids)
        docs = self.env['hospital.patient'].browse(docids[0])
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        appointment_list = []
        for app in appointments:
            vals = {
                'name': app.name,
                'notes': app.notes,
                'appointment_date': app.appointment_date
            }
            appointment_list.append(vals)
            # the report is waiting for docs, appointment line...
        return {
            'doc_model': 'hospital.patient',
            'docs': docs,
            'appointment_list': appointment_list,
        }
