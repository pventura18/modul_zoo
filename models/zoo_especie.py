from odoo import models, fields

class Especie(models.Model):
    _name = 'especie.especie'

    familia = fields.Char(string='Familia', required=True)
    nom_cientific = fields.Char(string='Nom Cientific', required=True)
    nom_vulgar = fields.Char(string='Nom Vulgar', required=True)
    perill = fields.Char(string='Perill', required=True)