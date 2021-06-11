from odoo import api, fields, models


class IutCours(models.Model):
	_name = 'iut.course'
	_description = 'Liste des cours'

	name = fields.Char('Nom du cours', required=True)
	

