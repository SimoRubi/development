# -*- coding: utf-8 -*-
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.product'

    children = fields.Many2one(comodel_name='onchange_proof.child')


class ModelName(models.Model):
    _name = 'child'

    name = fields.Char()
    parent_id = fields.Many2one(comodel_name='parent')
    product_id = fields.Many2one(comodel_name='product.product')
    seller_ids = fields.Many2many(comodel_name='product.supplierinfo')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        self.seller_ids = self.product_id.seller_ids
