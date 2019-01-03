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
     _("Raw Material Consumed/Supplied") + ":Link/Item:230",
     _("Qty Consumed/Supplied") + ":Float:180",
     _("Item Manufactured/Received") + ":Link/Item:230",
     _("Qty Manufactured/Received") + ":Float:180"
     ]
    else:
     return [
     _("Posting Date") + ":Date:100",
     _("ID") + ":Link/Stock Entry:140",
     _("Raw Material Consumed/ Supplied") + ":Data:220",
     _("Qty Supplied (Kg's)") + ":Float:120",
     _("Item Manufactured/Received") + ":Data:240",
     _("Qty Received (No's)") + ":Float:130",
     _("==>") + ":Data:3",
     _("Raw Material to be Consumed/Supplied") + ":Data:260",
     _("BOM CF") + ":Float:60",
     _("Qty to be Consumed/Supplied") +":Float:220",
     _("Item Difference(0,1)") + ":Data:160",
     _("Qty Difference(0,1)") + ":Data:120"
     ]

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
                   "To Be Programmed",
                   "B.qty",
                   "=>",
                   E.item_name,
                   E.qty,
                   B.qty*E.qty,
                   if(B.item_name=E.item_name,0,1),
                   if(B.qty=B.qty*E.qty,0,1)
                                      

                   FROM
                   `tabStock Entry` AS A,
                   `tabStock Entry Detail` AS B,
                   `tabItem` AS C,
                   `tabBOM` AS D,
                   `tabBOM Item` AS E

                   WHERE
                   A.name=B.parent
                   && B.item_name=C.item_name
                   && A.bom_no=D.name
                   && D.name=E.parent
                   && A.posting_date >= '%s' && A.posting_date <= '%s' 
                   && C.item_group = '%s' 
                   && A.purpose = '%s'
                   ORDER BY B.item_code ASC, A.name ASC """  %(from_date,to_date,item_group,consumption_type), as_list=1)
#              1111111111111111111111111111111111111111111111111111111111111111111111111111111
               elif filters.get("details")=="Less Details":
#              11111111111111111111111111111111111111111111111111111111111111111111111111111111
                   return frappe.db.sql("""
                   SELECT
                   B.item_name,
                   sum(B.qty),
                   "To Be Programed",
                   "To be programed"

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
                   sum(C.consumed_qty),
                   B.item_name,
                   sum(B.qty)

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
                   GROUP BY B.item_name 
                   ORDER BY D.item_name ASC """ %(from_date,to_date,item_group), as_list=1)

               elif filters.get("details")=="More Details":
                   return frappe.db.sql("""
                   SELECT DISTINCT
                   A.posting_date,
                   A.name,
                   D.item_name,
                   C.consumed_qty,
                   B.item_name,
                   B.qty,
                   "=>",
                   F.item_name,
                   F.qty,
                   F.qty*B.qty,
                   if(F.item_name=D.item_name,0,1),
                   if(C.consumed_qty=(B.qty*F.qty),0,1)

                   FROM
                   `tabPurchase Receipt` AS A,
                   `tabPurchase Receipt Item` AS B,
                   `tabPurchase Receipt Item Supplied` AS C,
                   `tabItem` AS D,
                   `tabBOM` AS E,
                   `tabBOM Item` AS F

                   WHERE
                   A.name=B.parent
                   && A.name=C.parent
                   && D.name=C.rm_item_code
                   && B.bom=E.name
                   && E.name=F.parent
                   && A.posting_date >= '%s' && A.posting_date <= '%s'
                   && D.item_group='%s'
                   ORDER BY D.item_name ASC,A.name ASC """ %(from_date,to_date,item_group), as_list=1)
#       1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 
#-----------------------------------------------------------------------------------------------------------
