# -*- coding: utf-8 -*-
{
    'name': "Rainbow Desktop Link",
    'summary': """
        Create products from Autodesk Vault Items
        """,
    'description': """
        Create products from Autodesk Vault Items
        """,
    'author': "Arnau Carbonell",
    'category': 'Inventory',
    'version': '16.0.0.0.0',
    'depends': [
        'stock'
    ],

    'data': [
        # VIEWS
        'views/product_views.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'license': 'Other proprietary',
    'installable': True,
    'application': False,
}
