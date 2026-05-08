# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Discord Module',
    'version': '0.1',
    'category': 'Uncategorized',
    'sequence': 15,
    'summary': 'Send Discord Messages',
    'website': 'https://www.danielspresian.dev/',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/discord_view.xml',
        'views/discord_menus.xml'
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