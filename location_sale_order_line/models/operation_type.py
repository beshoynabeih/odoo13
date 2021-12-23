from odoo import api, fields, models


class OperationType(models.Model):
    _inherit = 'stock.picking.type'

    default_operation_type = fields.Boolean(help='Default Operation type for sales')
