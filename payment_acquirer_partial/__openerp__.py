# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) LasLabs, Inc [https://laslabs.com]. All Rights Reserved
#
##############################################################################
#
#    Collaborators of this module:
#       Written By: Dave Lasley <dave@laslabs.com>
#
##############################################################################
#
#    This project is mantained by Medical Team:
#    https://repo.laslabs.com/projects/ODOO/repos/payment
#
##############################################################################
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
    'name': "Partial Invoice Payments in Portal",
    'license': 'AGPL-3',
    'author': "LasLabs",
    'website': "https://laslabs.com",
    'category': 'Payment',
    'version': '9.0.1.0.0',
    'depends': [
        'payment',
    ],
    'data': [
        'wizards/payment_acquirer_partial_wizard_view.xml',
    ],
    'installable': False,
    'application': False,
}
