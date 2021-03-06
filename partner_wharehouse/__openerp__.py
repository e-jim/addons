# -*- coding: utf-8 -*-
##############################################################################
#
#    Business Open Source Solution
#    Copyright (C) 2018 Coop IT Easy SCRLfs.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Partner Warehouse",
    "version": "9.0.1.0",
    "depends": [
        'base',
        'sale',
        'sale_stock',
    ],
    "author": "Rémy TAYMANS <remy@coopiteasy.be>",
    "category": "",
    "website": "www.coopiteasy.be",
    "license": "AGPL-3",
    "description": """
    Let the warehouse of the sale order be set accordingly to a default
    warehouse set on the partner.
    """,
    'data': [
        'views/res_partner.xml',
    ],
    'installable': True,
}
