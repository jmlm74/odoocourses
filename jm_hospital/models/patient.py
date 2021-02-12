from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


# inheriting standard classes --> change the methods without changing source code
#                             --> Add field in view without changing source
class ResPartners(models.Model):
    _inherit = 'res.partner'

    # How to OverRide Create Method Of a Model
    # https://www.youtube.com/watch?v=AS08H3G9x1U&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=26
    @api.model
    def create(self, vals_list):
        res = super(ResPartners, self).create(vals_list)
        print("yes working")
        # do the custom coding here
        return res

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
    appointment_count = fields.Integer(string='Appointment', compute='get_appointment_count')
    active = fields.Boolean("Active", default=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    email_id = fields.Char(string="Email")
    user_id = fields.Many2one('res.users', string="PRO")
    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female'),
        ], string="Doctor Gender")
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

    # Making compute field editable using inverse function
    # https://www.youtube.com/watch?v=NEr6hUTrn84&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=47
    def _inverse_upper_name(self):
        for rec in self:
            rec.patient_name = rec.patient_name_upper.lower() if rec.patient_name_upper else False

    # Action For Smart Button
    # https://www.youtube.com/watch?v=I93Lr-bprIc&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=19
    def open_patient_appointments(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
           # 'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

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

    # How to Write Onchange Functions
    # https://www.youtube.com/watch?v=qyRhjyp1MeE&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=39
    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        for rec in self:
            if rec.doctor_id:
                rec.doctor_gender = rec.doctor_id.gender

    # https://www.youtube.com/watch?v=-1r3WSwtqxQ
    def name_get(self):
        # name get function for the model executes automatically
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.name_seq, rec.patient_name)))
        return res

    # Sending Email in Button Click
    # https://www.youtube.com/watch?v=CZVRmtv6re0&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=44
    def action_send_card(self):
        # sending the patient report to patient via email
        template_id = self.env.ref('jm_hospital.patient_card_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    # Function which is executed using the Cron Job/ Scheduled Action
    # https://www.youtube.com/watch?v=_P_AVSNr6uU&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=52
    @api.model
    def test_cron_job(self):
        print("Abcd") # print will get printed in the log of pycharm
        #code accordingly to execute the cron

    # Print PDF Report From Button Click in Form
    # https://www.youtube.com/watch?v=Dc8GDj7ygsI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=67
    def print_report(self):
        return self.env.ref('jm_hospital.report_patient_card').report_action(self)
