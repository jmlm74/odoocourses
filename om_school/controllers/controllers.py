# -*- coding: utf-8 -*-
# from odoo import http


# class OmSchool(http.Controller):
#     @http.route('/om_school/om_school/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_school/om_school/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_school.listing', {
#             'root': '/om_school/om_school',
#             'objects': http.request.env['om_school.om_school'].search([]),
#         })

#     @http.route('/om_school/om_school/objects/<model("om_school.om_school"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_school.object', {
#             'object': obj
#         })
