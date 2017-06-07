# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"
    _name = "product.product"

    company_id = fields.Many2one(
        related='product_tmpl_id.company_id',
    )
    company_ids = fields.Many2many(
        related='product_tmpl_id.company_ids',
    )
