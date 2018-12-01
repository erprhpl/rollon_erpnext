# Copyright (c) 2013, Biradar Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
        columns=get_columns(filters)
        data=get_data(filters)
#        conditions=get_conditions(filters)
	return columns, data

def get_columns(filters):
 if filters.get("details"):
  if filters.get("details")=="More Details":
    return [
      _("Process No") + ":Data:80",
      _("Item Code") + ":Link/Item:140",
      _("Item Name") + ":Data:270",
      _("ROLLON Code") + ":Data:130",
      _("Item Group") + ":Data:130",
      _("description") + ":Data:250"
   ]
  else:
   return [
    _("Item Group") + ":Data:130",
    _("Total Item Masters") + ":Float:150"
   ]

def get_data(filters):
 if filters.get("details"):
  if filters.get("details")=="More Details":
    if filters.get("item_group"):
     item_group=filters.get("item_group")
     return frappe.db.sql("""
      SELECT
      A.process_no,
      A.name,
      A.item_name,
      A.rollon_code,
      A.item_group,
      A.description
  
      FROM
      `tabItem` AS A
  
      WHERE
      A.item_group = '%s'
      ORDER BY A.rollon_code DESC, A.process_no DESC """ %(item_group), as_list=1)

    else:
     return frappe.db.sql("""
      SELECT
      A.process_no,
      A.name,
      A.item_name,
      A.rollon_code,
      A.item_group,
      A.description
  
      FROM
      `tabItem` AS A
      ORDER BY A.rollon_code DESC, A.process_no DESC """ ) 
  else:
    return frappe.db.sql("""
    SELECT DISTINCT
    A.item_group,
    count(A.name)
    
    FROM
    `tabItem` AS A
    GROUP BY A.item_group  """ )
