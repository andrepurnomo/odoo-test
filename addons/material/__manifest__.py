{
    'name': 'Material Registration',
    'version': '14.0.0',
    'summary': 'Module for Material Registration',
    'description': 'Register materials with code, name, type, price and supplier',
    'category': 'Inventory',
    'author': 'Andre Agung Purnomo',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
