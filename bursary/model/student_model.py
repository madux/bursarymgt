# -*- coding: utf-8 -*-

# This module is used to allow patient book from signed in

from openerp import models, fields, api

class bursaryBook(models.Model):
    _name = 'student.book'


    #name = fields.Char('Name', required=True)
    #patient_id = fields.Many2one('medical.patient', string = 'Patient ID')
    #is_done
    #health = fields.Many2one('res.partner', string='Health Center')
    name = fields.Char('Name', required=True)
    student_id = fields.Char('Student ID', required=True)
    #active
    #responsible = fields.Many2one('res.users', 'Responsible', readonly=True)
    department = fields.Char('Department')
    guardian_physician = fields.Char('Guidance')
    department = fields.Many2one('res.partner', string='Department')
    faculty = fields.Many2one('res.partner', string='Department')
    hod = fields.Many2one('res.partner', string='Head of Department')
    dopayment = fields.Datetime('Date of Payment', required =True)
    mod = fields.Many2one('res.partner', string= 'Mode of Entry')
    #session = fields.Many2one('res.partner', string= 'Session')
    dob = fields.Datetime('Date of Admission', required =True)
    payment_is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    @api.one
    def do_toggle_done(self):
        self.active = not self.active
        return True
    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active'})
        return True




