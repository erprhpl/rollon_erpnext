# Copyright (c) 2013, Biradar Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate


def execute(filters=None):
	columns, data = [], []
        columns = get_columns()
        data = get_data()
	return columns, data

def get_columns():
 return [
  _("ID") + ":Link/BOM:200",
  _("Item Name") + ":Data:250",
  _("ROLLON Code") + ":Data:100",
  _("Item Group") + ":Data:130"
  ]

def get_data():
 return frappe.db.sql("""
  SELECT
  A.name,
  B.item_name,
  B.rollon_code,
  B.item_group

  FROM
  `tabBOM` AS A,
  `tabItem` AS B
  
  WHERE
  A.item_name=B.item_name
  
  ORDER BY B.rollon_code ASC, B.name ASC """)
