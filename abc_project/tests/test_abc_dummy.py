"""Test dummy functions """
import unittest
# from dotenv import load_dotenv
# from abcapp.module_app import process_data

# load_dotenv()  # Loads variables from .env

class TestAbcDummy(unittest.TestCase):
    def test_dummy_data(self):
        self.assertEqual("dummy", "DUMMY") # will fail
    def test_dummy_data1(self):
        self.assertEqual("dummy", "dummy")
    
class TestAbcDummy2(unittest.TestCase):
    def test_dummy_data2(self):
        self.assertEqual("dummy2", "dummy2")
    def test_dummy_data2b(self):
        self.assertEqual("dummy2b", "dummy") # will fail
