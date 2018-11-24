# Copyright (c) 2013, MN Technique and contributors
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
#         if filters.get("details"):
#          return [
#            if filters.get("details")=="Low Details":
#             return [
#              _("Raw Material Consumed") + ":Link/Item:230",
#              _("Qty consumed") + ":Float:120"
#             ]
#            elif filters.get("details")=="More Details":
#             return [
              _("Posting Date") + ":Date:100",
              _("ID") + ":Data:120",
              _("Raw Material Supplied") + ":Data:180",             
              _("Qty Supplied") + ":Float:100",
              _("Item Received") + ":Data:230",
              _("Qty Received") + ":Float:100"
    ]

def get_data(filters):
    if filters.get("from_date","to_date"):
        from_date=filters.get("from_date")
        to_date=filters.get("to_date")
    if filters.get("item_group"):
        item_group=filters.get("item_group")
    if filters.get("consumption_type"):
        if filters.get("consumption_type")=="Inhouse Consumption":
            consumption_type="Manufacture"
            return frappe.db.sql("""
            SELECT DISTINCT
            B.item_name,SUM(B.qty),B.qty,B.qty,B.qty,B.qty

            FROM
            `tabStock Entry` AS A,
            `tabStock Entry Detail` AS B,
            `tabItem` AS C
            WHERE
            A.name=B.parent
            && B.item_name=C.item_name
            && A.posting_date >= '%s' && A.posting_date <= '%s'
            && C.item_group = '%s' && A.purpose = '%s'
            ORDER BY B.item_name ASC """ %(from_date,to_date,item_group,consumption_type), as_list=1)

        elif filters.get("consumption_type")=="Supplier Consumption":
            return frappe.db.sql("""
            SELECT DISTINCT
            D.item_name,C.consumed_qty

            FROM
            `tabPurchase Receipt` AS A,
            `tabPurchase Receipt Item` AS B,
            `tabPurchase Receipt Item Supplied` AS C,
            `tabItem` AS D

            WHERE
            A.name=B.parent
            && A.name=C.parent
            && D.name=C.rm_item_code
            && A.posting_date >= '%s' && A.posting_date <= '%s'
            && D.item_group='%s'
            ORDER BY D.item_name ASC """ %(from_date,to_date,item_group), as_list=1)
    return
