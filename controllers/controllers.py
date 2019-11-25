# -*- coding: utf-8 -*-
from odoo import http

# class Competitos(http.Controller):
#     @http.route('/competitos/competitos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/competitos/competitos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('competitos.listing', {
#             'root': '/competitos/competitos',
#             'objects': http.request.env['competitos.competitos'].search([]),
#         })

#     @http.route('/competitos/competitos/objects/<model("competitos.competitos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('competitos.object', {
#             'object': obj
#         })