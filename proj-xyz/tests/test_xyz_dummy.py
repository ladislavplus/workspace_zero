"""Test dummy functions """
import unittest
from glob_utils.helpers import calculate_dummy, get_global_text

class TestXyzDummy(unittest.TestCase):
    def test_dummy_data(self):
        self.assertEqual("dummy", "dummy") # will fail
    def test_dummy_data2(self):
        self.assertEqual(get_global_text(), "global_text_variable")
    def test_dummy_data2b(self):
        self.assertEqual(calculate_dummy(2), 4)

