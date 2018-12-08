// Copyright (c) 2016, Biradar Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["CR Stock Ageing"] = {
	"filters": [
        {
        "fieldname":"range",
        "label": ("Range"),
        "fieldtype":"Select",
        "options":["0-30","30-60","60-90","90-180"],
        "default":"0-30"
        }
	]
}
