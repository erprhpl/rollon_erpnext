frappe.query_reports["CR Item Masters"] = {
    "filters":[

    {
    "fieldname":"details",
    "label" :("Details"),
    "fieldtype":"Select",
    "options":["Less Details","More Details"],
    "default":"More Details"
    },

    {
    "fieldname":"item_group",
    "label":("Item Group"),
    "fieldtype":"Link",
    "options":"Item Group"
    }
]
}
