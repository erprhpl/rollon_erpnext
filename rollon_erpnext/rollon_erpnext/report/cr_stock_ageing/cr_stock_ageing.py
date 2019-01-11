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
    _("Item Name") + ":Link/Item:300",
    _("Stock Balance") + ":Float:120"
    ]

def get_data(filters):
   if filters.get("item_group"):
    return frappe.db.sql ("""
    SELECT
    A.item_name,
    A.item_name
   
    FROM 
    `tabItem` AS A
    
    Where
    A.item_group='%s'

    ORDER BY A.item_name ASC """ %("item_group"), as_list=1)

