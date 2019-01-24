// Copyright (c) 2016, Biradar Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["CR Purchase Stock"] = {
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
      "fieldtype":"Link",
      "options":"Item Group",
      "default":"Raw Material"
      }, 
      {
      "fieldname":"purchase_type",
      "label":("Purchase Or Sales"),
      "fieldtype":"Select",
      "options":["Purchase","Sales","Stock Closed-Material Issue","Stock Received-Material Receipt"],
      "default":"Purchase"
      }
  ]
}
