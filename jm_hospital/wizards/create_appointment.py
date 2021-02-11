from odoo import models, fields


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment Wizard'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Date(string="Appointment Date")

    # Create Record From Code
    # https://www.youtube.com/watch?v=Jssb15ADeyg&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=40
    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
            'notes': 'Created From The Wizard/Code'
        }
        # creating appointments from the code
        self.env['hospital.appointment'].create(vals)
