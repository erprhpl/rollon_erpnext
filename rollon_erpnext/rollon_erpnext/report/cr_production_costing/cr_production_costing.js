frappe.query_reports["CR Production Costing"] = {
"filters": [
{
"fieldname":"from_date",
"label": __("FROM Date"),
"fieldtype": "Date",
"default": frappe.datetime.month_start(date)
},

{
"fieldname":"to_date",
"label": __("To Date"),
"fieldtype": "Date",
"default": get_today()
},

{
"fieldname":"cycle",
"label":__("Cycle"),
"fieldtype":"Link",
"options":"Cycle",
"default":""
},

{
"fieldname":"production_type",
"label":__("Production Type"),
"fieldtype":"Select",
"options":["Regular","D1","D2","D3","D4","S","RS"],
"default":"Regular"
}
]
}
