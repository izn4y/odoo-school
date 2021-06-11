from odoo import api, fields, models


class IutEleve(models.Model):
	_name = 'iut.student'
	_description = 'Gestion des eleves'

	firstname = fields.Char('Prénom')
	lastname = fields.Char('Nom')
	birthdate = fields.Date('Date de naissance')
	age = fields.Integer('Age')
	class_id = fields.Many2one('iut.class')