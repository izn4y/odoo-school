from odoo import api, fields, models


class IutEleve(models.Model):
	_name = 'iut.student'
	_description = 'Une courte description'

	firstname = fields.Char('Name')
	lastname = fields.Char('lastname')
	birthdate = fields.Date('Date de naissance')
	age = fields.Integer('Date de naissance')
	class_id = fields.Many2one('iut.class')