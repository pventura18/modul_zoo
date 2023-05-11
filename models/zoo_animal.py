from odoo import models, fields

class ZooAnimal(models.Model):
    _name = 'zoo.animal'

    continent_origen = fields.Char(string='Continent origen', required=True)
    data_naix = fields.Date(string='Data de naixement', required=True)
    pais_origen = fields.Char(string='Pais origen', required=True)
    sexe = fields.Selection([('m', 'Macho'), ('f', 'Hembra')], string='Sexe', required=True)