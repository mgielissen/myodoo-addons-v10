# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api, _


class eq_account_invoice(models.Model):
    _inherit = 'account.invoice'

    @api.one
    def _compute_street_house_no(self):
        """ Generate street and house no info for account_invoice """

        self.eq_street_house_no = ''
        if self.partner_id:
            if self.partner_id.street and self.partner_id.eq_house_no:
                self.eq_street_house_no = self.partner_id.street + ' ' + self.partner_id.eq_house_no
            elif self.partner_id.street:
                self.eq_street_house_no = self.partner_id.street


    @api.one
    def _compute_zip_city(self):
        """ Generate zip and city info for account_invoice """

        self.eq_zip_city = ''
        if self.partner_id:
            if self.partner_id.zip and self.partner_id.city:
                self.eq_zip_city = self.partner_id.zip + ' ' + self.partner_id.city
            elif self.partner_id.zip:
                self.eq_zip_city = self.partner_id.zip
            elif self.partner_id.city:
                self.eq_zip_city = self.partner_id.city

    @api.one
    def _compute_country(self):
        """ Generate country info for account_invoice """

        if self.partner_id and self.partner_id.country_id:
            self.eq_country = self.partner_id.country_id.name
        else:
            self.eq_country = ''

    eq_street_house_no = fields.Char(compute='_compute_street_house_no', string=" ", store=False)
    eq_zip_city = fields.Char(compute='_compute_zip_city', string=" ", store=False)
    eq_country = fields.Char(compute='_compute_country', string=" ", store=False)
    eq_head_text = fields.Html('Head Text')
    comment = fields.Html('Additional Information')
