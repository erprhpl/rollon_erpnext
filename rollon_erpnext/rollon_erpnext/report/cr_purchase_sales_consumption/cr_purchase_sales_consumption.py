# Copyright (c) 2013, Biradar Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
        columns=get_columns()
        data=get_data(filters)
	return columns, data
def get_columns():
 return [
  _("Item Name") + ":Data:200",
  _("Purchase Qty\Sales Qty") + ":Float:150",
  _("Supplier\Customer") + ":Data:180"
 ]

def get_data(filters):
      if filters.get("from_date","to_date"):
       from_date=filters.get("from_date")
       to_date=filters.get("to_date")
      if filters.get("item_group"):
       item_group=filters.get("item_group")
#      if filters.get("purchase_type"):

      if filters.get("purchase_type")=="Purchase":
        return frappe.db.sql("""
         SELECT
         B.item_name,
         sum(B.qty),
         A.supplier
         FROM
         `tabPurchase Receipt` AS A,
         `tabPurchase Receipt Item` AS B,
         `tabItem` AS C
         WHERE
         A.name=B.parent
         && B.item_code=C.item_code
         && A.posting_date>='%s' && A.posting_date<='%s'
         && C.item_group='%s'
         GROUP BY B.item_name ASC """ %(from_date,to_date,item_group), as_list=1)

      elif filters.get("purchase_type")=="Sales":
        return frappe.db.sql("""
         SELECT
         B.item_name,
         sum(B.qty),
         A.customer
         FROM
         `tabDelivery Note` AS A,
         `tabDelivery Note Item` AS B,
         `tabItem` AS C
         WHERE
         A.name=B.parent
         && B.item_code=C.item_code
         && A.posting_date>='%s' && A.posting_date<='%s'
         && C.item_group='%s'
         GROUP BY B.item_name ASC """ %(from_date,to_date,item_group), as_list=1)

      elif filters.get("purchase_type")=="Stock Closed-Material Issue":
         return frappe.db.sql("""
         SELECT
         B.item_name,
         sum(B.qty),
         B.s_warehouse
         FROM
         `tabStock Entry` AS A,
         `tabStock Entry Detail` AS B,
         `tabItem` AS C
         WHERE
         A.name=B.parent
         && B.item_code=C.item_code
         && A.posting_date>='%s' && A.posting_date<='%s'
         && C.item_group='%s'
         && A.purpose="Material Issue"
         GROUP BY B.item_name ASC """ %(from_date,to_date,item_group), as_list=1)

      elif filters.get("purchase_type")=="Stock Received-Material Receipt":
         return frappe.db.sql("""
         SELECT
         B.item_name,
         sum(B.qty),
         B.t_warehouse
         FROM
         `tabStock Entry` AS A,
         `tabStock Entry Detail` AS B,
         `tabItem` AS C
         WHERE
         A.name=B.parent
         && B.item_code=C.item_code
         && A.posting_date>='%s' && A.posting_date<='%s'
         && C.item_group='%s'
         && A.purpose="Material Receipt"
         GROUP BY B.item_name ASC """ %(from_date,to_date,item_group), as_list=1)
