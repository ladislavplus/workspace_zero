"""Test database functions using module_app."""
import unittest
from dotenv import load_dotenv
from abcapp.module_app import process_abc_data as process_data

load_dotenv()  # Loads variables from .env

class TestAbcDB(unittest.TestCase):
    def test_process_data(self):
        self.assertEqual(process_data("abc"), "ABC (admin)")
    