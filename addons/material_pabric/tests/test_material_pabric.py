# -*- coding: utf-8 -*-
 
from odoo.tests import common
 
class TestMaterialPabric(common.TransactionCase):

    def test_create_data(self):
        test_material = self.env['material.pabric'].create({
            'name': 'Celana formal',
            'material_type': 'jeans',
            'material_buy_price': 590,

        })

        self.assertEqual(test_material.name, 'Celana formal')
