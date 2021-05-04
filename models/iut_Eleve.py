from odoo import api, fields, models


class IutAgenda(models.Model):
	_name = 'iut.student'
	_description = 'Une courte description'

	firstname = fields.Char('Name')
	lastname = fields.Char('Name')
	birthdate = fields.Date('Date de naissance')
	age = fields.Integer('Date de naissance')

	class_id = fields.Many2one()
	
