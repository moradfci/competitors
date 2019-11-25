# -*- coding: utf-8 -*-

from odoo import models, fields, api

class competitos(models.Model):
    _name = 'competitos.competitos'

    name = fields.Char()
    description = fields.Text()
