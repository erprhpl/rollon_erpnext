// Copyright (c) 2016, MN Technique and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Raw Material Consumption"] = {
    "filters": [
        {
        "fieldname":"from_date",
        "label":("From Date"),
        "fieldtype":"Date",
        "default":frappe.datetime.month_start(date)
//        "default":frappe.defaults.get_user_default("year_start_date")
        },
        {
        "fieldname":"to_date",
        "label":("To Date"),
        "fieldtype":"Date",
        "default":get_today()
        },
        {
        "fieldname":"consumption_type",
        "label":("Consumption Type"),
        "fieldtype":"Select",
        "options":["Inhouse Consumption","Supplier Consumption"],
        "default":"Inhouse Consumption"
        },

        {
        "fieldname":"details",
        "label":("Details"),
        "fieldtype":"Select",
        "options":["Less Details","More Details"],
        "default":"Less Details"
        },        
        {
        "fieldname":"item_group",
        "label":("Item Group"),
        "fieldtype":"Read Only",
        "options":["Raw Material","SFG"],
        "default":"Raw Material"
        }
//        {
//        "fieldname":"supplier_balance",
//        "label":("Supplier Balance"),
//        "fieldtype":"Select",
//        "options":["","Less Details","More Details"],
//        "default":""
//        }

    ]

}
