# -*- coding: utf-8 -*-
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class Father(models.Model):
    _name = 'parent'

    name = fields.Char()
    children_ids = fields.One2many(comodel_name='child', inverse_name='parent_id')
