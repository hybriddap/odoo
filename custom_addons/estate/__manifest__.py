# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Real Estate',
    'version': '1.9',
    'category': 'Uncategorized',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'website': 'https://www.odoo.com/app/crm',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_view.xml',
        'views/estate_menu.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
    },
    'author': 'Dap',
    'license': 'LGPL-3',
}