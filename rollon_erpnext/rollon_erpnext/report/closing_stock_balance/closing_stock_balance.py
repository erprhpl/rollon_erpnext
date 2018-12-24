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
    _("Purchase") + ":Float:100",
    _("Consumption") + ":Float:120",
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
    A.item_code,
    E.actual_qty,
    A.actual_qty,
    A.outgoing_rate,
    sum(A.qty_after_transaction),
    A.stock_value

    FROM
    `tabStock Ledger Entry` AS A,
    `tabItem` AS B,
    `tabPurchase Receipt` AS C,
    `tabPurchase Receipt Item` AS D,
    `tabBin` AS E
    
    WHERE
    A.item_code=B.item_code
    && D.item_name=B.item_name
    && E.item_code=A.item_code
    && A.posting_date>='%s' && A.posting_date<='%s'
    && B.item_group='%s'
    GROUP BY B.item_group
    ORDER BY B.item_name """ %(from_date,to_date,item_group), as_list=1)
