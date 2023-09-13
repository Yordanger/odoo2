from email.policy import default
from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property"

    name = fields.Char(required=True)
    expected_price = fields.Float(required=True)
    garden_orientation = fields.Selection(string='Garden orientation', selection=[
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default='east')
    
    postcode = fields.Char()
    date_availability = fields.Date() #preguntar sobre este campo =>
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facade = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    
