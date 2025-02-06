from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestMaterial(TransactionCase):
    def setUp(self):
        super(TestMaterial, self).setUp()
        self.partner = self.env['res.partner'].create({
            'name': 'Test Supplier',
            'email': 'supplier@test.com'
        })

        self.material = self.env['material.registration'].create({
            'material_code': 'M001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150.0,
            'supplier_id': self.partner.id
        })

    def test_create_material(self):
        """Test material creation"""
        self.assertEqual(self.material.material_code, 'M001')
        self.assertEqual(self.material.material_name, 'Test Material')
        self.assertEqual(self.material.material_type, 'fabric')
        self.assertEqual(self.material.material_buy_price, 150.0)
        self.assertEqual(self.material.supplier_id, self.partner)

    def test_material_buy_price_constraint(self):
        """Test material buy price constraint"""
        with self.assertRaises(ValidationError):
            self.env['material.registration'].create({
                'material_code': 'M002',
                'material_name': 'Test Material 2',
                'material_type': 'jeans',
                'material_buy_price': 50.0,  # Should raise ValidationError
                'supplier_id': self.partner.id
            })

    def test_material_type_selection(self):
        """Test material type selection values"""
        valid_types = ['fabric', 'jeans', 'cotton']
        self.assertIn(self.material.material_type, valid_types)

    def test_name_get(self):
        """Test material name display"""
        self.assertEqual(self.material.material_name, 'Test Material')

    def test_required_fields(self):
        """Test required fields validation"""
        with self.assertRaises(Exception):
            self.env['material.registration'].create({
                'material_code': 'M003',
                'material_name': False,
                'material_type': False,
                'material_buy_price': False,
                'supplier_id': False
            })
