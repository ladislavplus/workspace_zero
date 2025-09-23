"""Test dummy functions """
import unittest
from abc_app.module_app import process_abc_data
from abc_app.utils.my_useful import greet



class TestAbcDummy(unittest.TestCase):
    # def test_dummy_data(self):
      #  self.assertEqual("dummy", "DUMMY") # will fail
    def test_dummy_data1(self):
        self.assertEqual("dummy", "dummy")
    
class TestAbcDummy2(unittest.TestCase):
    def test_dummy_data2(self):
        self.assertEqual(process_abc_data("dummy2"), "DUMMY2 (admin)")
    def test_dummy_data2b(self):
        self.assertEqual(greet("dummy"), "Hello, dummy!")

