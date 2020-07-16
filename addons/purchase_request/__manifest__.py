# Copyright 2018-2019 ForgeFlow, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Purchase Request",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "version": "13.0.2.1.1",
    "summary": "Use this module to have notification of requirements of "
               "materials and/or external services and keep track of such "
               "requirements.",
    "category": "Purchase Management",
    "depends": ["purchase"],
    "data": [
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/purchase_request.xml',
        'views/purchase_request_lines.xml',
    ],
    "demo": [],
    "license": "LGPL-3",
    "installable": True,
    "application": True,
}