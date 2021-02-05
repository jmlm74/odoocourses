from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


# Inheriting the Sale Order Model and Adding New Field
# https://www.youtube.com/watch?v=z1Tx7EGkPy0&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=9
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    """
    @api.multi
    def action_confirm(self):
        print("odoo mates")
        res = super(SaleOrderInherit, self).action_confirm()
        return res
    """
    patient_name = fields.Char(string='Patient Name')
    is_patient = fields.Boolean(string='Is Patient')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'
    # rec.xml_id = res.get(rec.id)

    #name = fields.Char(string="Contact Number")
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection([
                               ('male', 'Male'),
                               ('fe_male', 'Female'),
                              ], default='male', string="Gender")
    age_group = fields.Selection([
                                  ('major', 'Major'),
                                  ('minor', 'Minor'),
                                 ], string="Age Group", compute='set_age_group', store=True)
    patient_name = fields.Char(string='Name', required=True, track_visibility="always")
    # add  track visibility (already done in my copy/paste !
    patient_age = fields.Integer('Age', track_visibility="always", group_operator=False)
    #patient_age2 = fields.Float(string="Age2")
    notes = fields.Text(string="Registration Note")
    image = fields.Binary(string="Image", attachment=True)
    #appointment_count = fields.Integer(string='Appointment', compute='get_appointment_count')
    #active = fields.Boolean("Active", default=True)
    #doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    #email_id = fields.Char(string="Email")
    #user_id = fields.Many2one('res.users', string="PRO")
    #doctor_gender = fields.Selection([
    #    ('male', 'Male'),
    #    ('fe_male', 'Female'),
    #    ], string="Doctor Gender")
    patient_name_upper = fields.Char(compute='_compute_upper_name', inverse='_inverse_upper_name')

    # Overriding the create method to assign sequence for the record
    # https://www.youtube.com/watch?v=ZfKzmfiqeg0&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=8
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

    # compute function in Odoo
    # https://www.youtube.com/watch?v=Mg80GxrKDOc&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=11
    @api.depends('patient_name')
    def _compute_upper_name(self):
        for rec in self:
            rec.patient_name_upper = rec.patient_name.upper() if rec.patient_name else False

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    # Add Constrains For a Field
    # https://www.youtube.com/watch?v=ijS-N1CdiWU&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=14
    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age < 5:
                raise ValidationError(_('The Age Must be Greater Than 5..!'))