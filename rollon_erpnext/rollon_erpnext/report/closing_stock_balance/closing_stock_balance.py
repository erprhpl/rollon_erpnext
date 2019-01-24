# Copyright (c) 2013, Biradar Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
        columns=get_columns()
        data=get_data(filters)
	return columns, data

def get_columns():
    return [
    _("Item Name") + ":Data:250",
    _("Opening Stock") + ":Float:120",
    _("Purchase Stock") + ":Float:100",
    _("Sales Stock") + ":Float:100",
    _("Consumed Stock") + ":Float:120",
    _("Closing Stock") + ":Float:120",
    _("Supplier Balance") + ":Float:120"
    ]

def get_data(filters):
    if filters.get("from_date", "to_date"):
     from_date=filters.get("from_date")
     to_date=filters.get("to_date") 
    if filters.get("item_group"):
     item_group=filters.get("item_group")
    return frappe.db.sql("""
           SELECT
           I.item_group,
           "0",
           sum(PRI.qty),
           "0",
           "0",
           "0",
           "0"

           FROM 
           `tabItem` AS I,
           `tabPurchase Receipt` AS PR,
           `tabPurchase Receipt Item` AS PRI
/*           `tabDelivery Note` AS DN,*/
/*           `tabDelivery Note Item` AS DNI*/
           
/*           LEFT JOIN I ON I.item_code=PRI.item_code*/
/*           INNER JOIN I ON (I.item_code)=(PRI.item_code)*/
             
           WHERE
           I.item_code=PRI.item_code
           && PR.name=PRI.parent
/*           && I.item_code=DNI.item_code*/
/*           && DN.name=DNI.parent*/
/*           && FROM I RIGHT JOIN DNI ON I.item_code=DNI.item_code */
           && PR.posting_date >= '%s' && PR.posting_date <= '%s' 
/*           && I.item_group = '%s'*/
           GROUP BY I.item_group
           ORDER BY I.item_group ASC """ %(from_date,to_date,item_group), as_list=1 )
