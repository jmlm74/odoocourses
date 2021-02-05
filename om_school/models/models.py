from odoo import models, fields, api


class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student table"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string='Age', required=False)
    guardian = fields.Char(string='Guardian', required=False)
    gender = fields.Selection([
                                ('male', 'M'),
                                ('female', 'F'),
                                ('other', 'O'),
                               ], required=False, string="Gender",
                                  default='male', help="Student Gender")
    image = fields.Binary(string='Image')