from odoo import models, fields

class ZooZoo(models.Model):
    _name = 'zoo.zoo'

    grandaria = fields.Integer(string='Tamany', required=True)
    nom = fields.Char(string='Nom', required=True)
    ciutat = fields.Char(string='Ciutat', required=True)
    pais = fields.Char(string='Pais', required=True)