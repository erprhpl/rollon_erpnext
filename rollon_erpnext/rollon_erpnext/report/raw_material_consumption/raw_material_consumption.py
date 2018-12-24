#copyright (c) 2013, Biradar Technologies
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
    columns, data = [], []
    columns=get_columns(filters)
    data=get_data(filters)
    return columns, data

#---------------------------------------------------------------------------------------------------------------
def get_columns(filters):
  if filters.get("details"):
    if filters.get("details")=="Less Details":
     return [
     _("Raw Material Consumed") + ":Link/Item:230",
     _("Qty Consumed") + ":Float:120"
     ]
    else:
     return [
     _("Posting Date") + ":Date:100",
     _("ID") + ":Link/Stock Entry:140",
     _("Raw Material Consumed/ Supplied") + ":Data:220",
     _("Qty Supplied (Kg's)") + ":Float:120",
     _("Item Manufactured/Received") + ":Data:240",
     _("Qty Received (No's)") + ":Float:130"
     ]

#  elif (filters.get("supplier_balance")):
#    return [
#    _("Raw Material Supplied") + ":Data:150",
#    _("Qty Supplied") + ":Float:100",
#    _("Qty Consumed") + ":Float:150",
#    _("Supplier Balance") + ":Float:150" 
#    ]

#------------------------------------------------------------------------------------------------------------------
def get_data(filters):
    if filters.get("from_date","to_date"):
        from_date=filters.get("from_date")
        to_date=filters.get("to_date")
    if filters.get("item_group"):
        item_group=filters.get("item_group")    
    if filters.get("consumption_type") :
        if filters.get("consumption_type")=="Inhouse Consumption":  
               consumption_type="Manufacture"
               if filters.get("details")=="More Details":
#              111111111111111111111111111111111111111111111111111111111111111111111111111111
                   return frappe.db.sql("""
                   SELECT
                   A.posting_date,
                   A.name,
                   case when C.item_group="Raw Material" then B.item_name end,
                   case when C.stock_uom="Kg" then B.qty end,
                   if (C.item_group<>"Raw Material", B.item_name,B.item_name),
                   B.qty
                   FROM
                   `tabStock Entry` AS A,
                   `tabStock Entry Detail` AS B,
                   `tabItem` AS C

                   WHERE
                   A.name=B.parent
                   && B.item_name=C.item_name
                   && A.posting_date >= '%s' && A.posting_date <= '%s' 
                   && C.item_group = '%s' 
                   && A.purpose = '%s'
                   ORDER BY B.item_code ASC """  %(from_date,to_date,item_group,consumption_type), as_list=1)
#              1111111111111111111111111111111111111111111111111111111111111111111111111111111
               elif filters.get("details")=="Less Details":
#              11111111111111111111111111111111111111111111111111111111111111111111111111111111
                   return frappe.db.sql("""
                   SELECT
                   B.item_name,
                   sum(B.qty)

                   FROM                                         
                   `tabStock Entry` AS A,
                   `tabStock Entry Detail` AS B,
                   `tabItem` AS C
                   
                   WHERE
                   A.name=B.parent
                   && B.item_name=C.item_name
                   && A.posting_date >= '%s' && A.posting_date <= '%s'
                   && C.item_group='%s' 
                   && A.purpose = "Manufacture"
                   ORDER BY B.item_name ASC """ %(from_date,to_date,item_group), as_list=1)
#              1111111111111111111111111111111111111111111111111111111111111111111111111111111111
        elif filters.get("consumption_type")=="Supplier Consumption":
#       111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
               if filters.get("details")=="Less Details":
                   return frappe.db.sql("""
                   SELECT DISTINCT
                   D.item_name,
                   sum(C.consumed_qty)

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
                   GROUP BY D.item_name 
                   ORDER BY D.item_name ASC """ %(from_date,to_date,item_group), as_list=1)

               elif filters.get("details")=="More Details":
                   return frappe.db.sql("""
                   SELECT DISTINCT
                   A.posting_date,
                   A.name,
                   D.item_name,
                   C.consumed_qty,
                   B.item_name,
                   B.qty

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
#       1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 
#-----------------------------------------------------------------------------------------------------------
