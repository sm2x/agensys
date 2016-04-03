from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Agency Transactions"),
			"items": [
				{
					"type": "doctype",
					"name": "Ad Campaigns",
					"description": _("Records customer RFQ and opportunity."),
				},
				{
					"type": "doctype",
					"name": "Media Plan",
					"description": _("Records Ad Campaign detailed plans."),
				},
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"description": _("All products and services."),
				},
				{
					"type": "page",
					"name": "Sales Browser",
					"icon": "icon-sitemap",
					"label": _("Item Group"),
					"link": "Sales Browser/Item Group",
					"description": _("Tree of Item Groups."),
					"doctype": "Item Group",
				},
				{
					"type": "doctype",
					"name": "Item Attribute",
					"description": _("Other characteristics of an item."),
				},
				{
					"type": "doctype",
					"name": "Item Price",
					"description": _("Multiple Item prices."),
					"route": "Report/Item Price"
				},
				{
					"type": "doctype",
					"name": "UOM",
					"label": _("Unit of Measure") + " (UOM)",
					"description": _("e.g. Unit, Sec, Hours, Days, Nos, Pkg")
				},

			]
		},
	      ]
