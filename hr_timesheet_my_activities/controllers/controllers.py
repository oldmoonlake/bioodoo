# -*- coding: utf-8 -*-
from odoo import http

# class HrTimesheetMyActivities(http.Controller):
#     @http.route('/hr_timesheet_my_activities/hr_timesheet_my_activities/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_timesheet_my_activities/hr_timesheet_my_activities/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_timesheet_my_activities.listing', {
#             'root': '/hr_timesheet_my_activities/hr_timesheet_my_activities',
#             'objects': http.request.env['hr_timesheet_my_activities.hr_timesheet_my_activities'].search([]),
#         })

#     @http.route('/hr_timesheet_my_activities/hr_timesheet_my_activities/objects/<model("hr_timesheet_my_activities.hr_timesheet_my_activities"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_timesheet_my_activities.object', {
#             'object': obj
#         })