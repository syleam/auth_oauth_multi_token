# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'auth_oauth_multi_token',
    'version': '1.0',
    'license': 'AGPL-3',
    'author': "Florent de Labarre",
    'summary': 'Multi token connection',
    'category': 'Tool',
    'website': 'www.iguana-yachts.com',
    'depends': ['auth_oauth'],
    'data': [
        'auth_oauth_multi_token.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
