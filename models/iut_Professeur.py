from odoo import api, fields, models


class IutProfesseur(models.Model):

	_name = 'res.partner'
	_description = 'Une courte description'

	class_ids = fields.Many2one()
