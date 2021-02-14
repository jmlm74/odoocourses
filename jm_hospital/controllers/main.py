from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class AppointmentController(http.Controller):

    @http.route('/jm_hospital/appointments', auth='user', type='json')
    def appointment_banner(self):
        return {
            'html': """
                    <div>
                        <link>
                        <center><h1><font color="red">Subscribe the channel.......!</font></h1></center>
                        <center>
                        <p><font color="blue"><a href="https://www.youtube.com/channel/UCVKlUZP7HAhdQgs-9iTJklQ/videos">
                            Get Notified Regarding All The Odoo Updates!</a></p>
                            </font></div></center> """
                                }


class WebsiteSaleInherit(WebsiteSale):
    # 1st install website_sale !
    # override shop method --> to show How-to
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
        print("Inherited Odoo Mates ....", res)
        return res


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
