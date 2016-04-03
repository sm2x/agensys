# -*- coding: utf-8 -*-
# Copyright (c) 2015, Hanstel Projects and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint
from frappe.model.document import Document

class MediaPlan(Document):
        def autoname(self):
                # concat first and last name
                self.name = " ".join(filter(None,
                        [cstr(self.get(f)).strip() for f in ["mp_adcampaign", "mp_channel"]]))

                # self.mp_profile = " + ".join(filter(None,
                #        [cstr(self.get(f)).strip() for f in ["ad_client", "ad_budget"]]))

                # concat party name if reqd
                for fieldname in ("ad_client"):
                        if self.get(fieldname):
                                self.name = self.name + " - " + cstr(self.get(fieldname)).strip()
                                break
