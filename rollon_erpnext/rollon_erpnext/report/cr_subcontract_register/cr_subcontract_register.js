// Copyright (c) 2016, Biradar Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["CR Subcontract Register"] = {
	"filters": [

      {
      "fieldname":"from_date",
      "label":("From Date"),
      "fieldtype":"Date",
      "default":frappe.datetime.month_start(date)
      },
      {
      "fieldname":"to_date",
      "label":("To Date"),
      "fieldtype":"Date",
      "default":get_today()     
      },
      {
      "fieldname":"item_group",
      "label":("Item Group"),
      "fieldtype":"Read Only",
      "options":"Item Group",
      "default":"Raw Material"
      }

]
}
