# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and Contributors
# See license.txt
<<<<<<< HEAD


import unittest

import frappe

test_records = frappe.get_test_records("Monthly Distribution")


class TestMonthlyDistribution(unittest.TestCase):
=======
import unittest

import frappe
from frappe.tests import IntegrationTestCase


class TestMonthlyDistribution(IntegrationTestCase):
>>>>>>> da09316d4c (fix: precision check for salvage value)
	pass
