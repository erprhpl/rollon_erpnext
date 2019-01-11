// Copyright (c) 2016, Biradar Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["CR Stock Ageing"] = {
	"filters": [
        {
        "fieldname":"range",
        "label": ("Range"),
        "fieldtype":"Select",
        "options":["0-30","31-60","61-90","91-180","181-Above"],
        "default":"0-30"
        },

        {
        "fieldname":"item_group",
        "label":("Item Group"),
        "fieldtype":"Link",
        "options":"Item Group",
        "default":"Raw Material"
        }


    ]

}
