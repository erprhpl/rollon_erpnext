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
      _("Date") + ":Date:100",
      _("Purchase Receipt") + ":Purchase Receipt:120",
      _("Item Received") + ":Data:200",
      _("Qty Received") + ":Float:100",
      _("Item Supplied") + ":Data:200",
      _("Qty Supplied") + ":Float:100",
      _("Supplier") + ":Data:150",
      _("Supplier Invoice No") + ":Data:120",
      _("Supplier Invoice Date") + ":Date:120",
      _("STE No") + ":Data:90",
      _("STE Date") + ":Date:90",
      _("Purchase Order") + ":Data:110",
      _("%Discount") + ":Data:80",
      _("Discount") + ":Data:120"
      ]

def get_data(filters):
  if filters.get("from_date","to_date"):
   from_date=filters.get("from_date")
   to_date=filters.get("to_date")
   return frappe.db.sql("""
     SELECT
     PR.posting_date,
     PR.name,
     PRI.item_name,
     PRI.qty,
     I.item_name,
     PRIS.consumed_qty,
     PR.supplier,
     PR.supplier_invoice_no,
     PR.supplier_invoice_date,
     PRI.stock_entry_no,
     PRI.stock_entry_date,
     PRI.purchase_order,
     PR.additional_discount_percentage,
     PR.discount_amount     


     FROM
     `tabPurchase Receipt` AS PR,
     `tabPurchase Receipt Item` AS PRI,
     `tabPurchase Receipt Item Supplied` AS PRIS,
     `tabItem` AS I
     WHERE
     PR.name=PRI.parent
     && PR.name=PRIS.parent
     && PRIS.rm_item_code=I.item_code
     && PR.posting_date>='%s' && PR.posting_date<='%s'
     ORDER BY PR.posting_date ASC """ %(from_date,to_date), as_list=1)
