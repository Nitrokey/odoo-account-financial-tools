# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2012 Therp BV (<http://therp.nl>).
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
    'name': 'Account Purchase Default',
    'version': '6.1.r103',
    'depends': [
        'base',
        'account'
    ],
    'author': 'Ronald Portier, Therp B.V.',
    'category': 'Accounting',
    'description': '''When entering purchase invoices directly, the user has
to select an account which will be used as a counterpart in the generated
move lines. However, each supplier will mostly be linked to one account. For
instance when ordering paper from a supplier that deals in paper, the counter-
part account will mostly be something like 'office expenses'. 
This module will add a default counterpart account to a partner (supplier
only), comparable to the similiar field in product. When a supplier invoice
is entered, withouth a product, the field from partner will be used as default.
''',
    'init_xml': [],
    'update_xml': [
        'view/res_partner_view.xml'
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
}
