"""Test dummy functions """
import unittest
# from dotenv import load_dotenv
from glob_utils.helpers import calculate_dummy, get_global_text

# load_dotenv()  # Loads variables from .env

class TestXyzDummy(unittest.TestCase):
    def test_dummy_data(self):
        self.assertEqual("dummy", "DUMMY") # will fail
    def test_dummy_data2(self):
        self.assertEqual(get_global_text(), "-check-")
    def test_dummy_data2b(self):
        self.assertEqual(calculate_dummy(2), 5) # will fail

