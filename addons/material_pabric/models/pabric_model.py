from odoo import api, fields, models, _ 
from odoo.exceptions import ValidationError

TYPE = [
    ('fabric', 'Fabric'),
    ('jeans', 'Jeans'),
    ('cotton', 'Cotton'),
]

class MaterialPabric(models.Model):
    _name = 'material.pabric'
    _description = 'Material Pabric'
    

    @api.model
    def _get_default_code_seq(self):
        return self.env['ir.sequence'].next_by_code('material.pabric.code')

    material_code = fields.Char(string="Material Code", default=_get_default_code_seq, required=True,)
    name = fields.Char(string="Material Name ", required=True,)
    material_type = fields.Selection(TYPE, 'Material Type', required=True)
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    material_buy_price = fields.Monetary(string="Material Buy Price",required=True)
    supplier = fields.Many2one('res.partner', string="Supplier",required=True)

    @api.constrains('material_buy_price')
    def _check_buy_price(self):
        for rec in self:
            if rec.material_buy_price <= 100:
                raise ValidationError(_("Material Buy Price Harus Lebih dari 100"))
        return True