from odoo import api, fields, models


class IutAgenda(models.Model):
	_name = 'iut.schedule'
	_description = 'Une courte description'

	name = fields.Char('Name', required=True)

	partner_id = fields.Many2one('res.partner', 'Employer id')
	model_id = fields.Many2one('iut.it.model', 'model id')
	room_id = fields.Many2one('iut.it.room', 'salle id')

	date_start = fields.Date('Horaire début')
	date_stop = fields.Date('Horaire fin')
	room = fields.Char('Salle de classe')
	class_id = fields.Many2one()
	course_id = fields.Many2one()
    