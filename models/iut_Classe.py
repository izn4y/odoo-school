from odoo import api, fields, models


class IutClasse(models.Model):
	_name = 'iut.class'
	_description = 'Gestion des classe'

	name = fields.Char('Nom classe')
	level = fields.Selection([('seconde', 'Seconde'), ('premiere', 'Première'),('terminale', 'Terminale'), ], 'Niveau', default='seconde', required=True)
	teacher_id = fields.Many2one('res.partner')
	student_ids = fields.One2many('iut.student','class_id')
