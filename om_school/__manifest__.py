# -*- coding: utf-8 -*-
{
    'name': "School Management",
    'sequence': 1,
    'license': 'LGPL-3',
    'summary': """Schhol Mgmt software""",
    'description': """Module to manage school""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra tools',
    'version': '14.0.0.1.0',
    'images': ['static/description/banner.png'],
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
