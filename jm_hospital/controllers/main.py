from odoo import http
from odoo.http import request


class Hospital(http.Controller):

    @http.route('/hospital/patient',  auth="public", website=True)
    def hospital_patient(self, **kwargs):
        print("Execution Here.........................")
        #return "Hello World"
        #doctor_rec = request.env['hospital.doctor'].sudo().search([])
        # print("doctor_rec...", doctor_rec)
        patients = request.env['hospital.patient'].sudo().search([])
        context = {'patients': patients}
        return http.request.render('jm_hospital.patients_page', context)
        #return http.request.render('om_hospital.create_patient', {'patient_name': 'Odoo Mates Test 123',
        #                                                          'doctor_rec': doctor_rec})
