# -*- coding: utf-8 -*-
# © 2019- Houssine BAKKALI - Coop IT Easy SCRLfs
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'Website Portal Sale v10 Fix',
    'version': '9.0.0.1',
    'category': 'E-commerce',
    'sequence': 95,
    'author': "Houssine BAKKALI - Coop IT Easy SCRLfs",
    'website': 'www.coopiteasy.be',
    'license': "AGPL-3",
    'summary': 'Fix unwanted button',
    'description': """

============================

This module fix the access rules problem for users on some partners. The button
pay now access the partner_id of the invoice
and for an unknown reason it raise an 403 error due to an access rule on the
res_partner model

    """,
    'depends': ['website_portal_sale_v10'],
    'data': [
        'views/website_portal_sale_v10_templates.xml',
    ],
    'installable': True,
}
