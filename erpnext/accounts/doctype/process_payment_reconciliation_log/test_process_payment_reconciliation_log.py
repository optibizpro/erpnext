# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestProcessPaymentReconciliationLog(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestProcessPaymentReconciliationLog(UnitTestCase):
	"""
	Unit tests for ProcessPaymentReconciliationLog.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestProcessPaymentReconciliationLog(IntegrationTestCase):
>>>>>>> da09316d4c (fix: precision check for salvage value)
	pass
