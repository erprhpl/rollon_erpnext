# Copyright (c) 2013, Biradar Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
        columns=get_columns()
        data=get_data()
	return columns, data

def get_columns():
    return [
    _("Item Name") + ":Data:250",
    _("Opening Stock") + ":Float:120",
    _("Purchase Stock") + ":Float:100",
    _("Consumed Stock") + ":Float:120",
    _("Closing Stock") + ":Float:120",
    _("Supplier Balance") + ":Float:120"
    ]

def get_data():
#    if filters.get("from_date", "to_date"):
#     from_date=filters.get("from_date")
#     to_date=filters.get("to_date") 
#    if filters.get("item_group"):
#     item_group=filters.get("item_group")
    return frappe.db.sql("""
    SELECT
    A.item_code,
    "0",
    "0",
    "0",
    "0",
    "0"

    FROM
    `tabItem` AS A """)
