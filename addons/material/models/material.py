from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = 'material.registration'
    _description = 'Material Registration'
    _rec_name = 'material_name'
    _order = 'material_code asc'

    TYPE_SELECTION = [
        ('fabric', _('Fabric')),
        ('jeans', _('Jeans')),
        ('cotton', _('Cotton'))
    ]

    material_code = fields.Char(
        string='Material Code',
        required=True,
        help="Enter unique identifier code for the material"
    )
    material_name = fields.Char(
        string='Material Name',
        required=True,
        help="Enter the full name of the material"
    )
    material_type = fields.Selection(
        TYPE_SELECTION,
        string='Material Type',
        required=True,
        help="Select the type of material from available options"
    )
    material_buy_price = fields.Float(
        string='Material Buy Price',
        required=True,
        help="Enter the purchase price - must be greater than 100"
    )
    supplier_id = fields.Many2one(
        'res.partner',
        string='Related Supplier',
        required=True,
        help="Select the supplier who provides this material"
    )

    @api.constrains('material_buy_price')
    def _check_material_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise ValidationError(
                    _('Material Buy Price cannot be less than 100!')
                )
