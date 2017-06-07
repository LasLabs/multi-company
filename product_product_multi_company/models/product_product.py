# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class ProductProduct(models.Model):
    _inherit = ["multi.company.abstract", "product.product"]
    _name = "product.product"
    _description = "Product Variant (Multi-Company)"
