from odoo import api, fields, models


class IutAgenda(models.Model):
    _name = 'iut.schedule'
    _description = 'Une courte description'

    date_start = fields.Date('Horaire début')
    date_stop = fields.Date('Horaire fin')
    room = fields.Char('Salle de classe')
    class_id = fields.Many2one('iut.class')
    course_id = fields.Many2one('iut.course', required=True)
