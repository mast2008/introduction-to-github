from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_registry = fields.Char("CR No.")
