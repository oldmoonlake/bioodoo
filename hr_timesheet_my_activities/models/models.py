# -*- coding: utf-8 -*-

from odoo import models, fields, api
# class hr_timesheet_my_activities(models.Model):
#     _name = 'hr_timesheet_my_activities.hr_timesheet_my_activities'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
