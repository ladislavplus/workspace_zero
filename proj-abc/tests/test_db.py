"""Test database functions using module_app."""
import unittest
from dotenv import load_dotenv
from abc_app.module_app import process_abc_data as process_data
from abc_app.database import get_db_dummy_data as get_db_data


load_dotenv()  # Loads variables from .env

class TestAbcDB(unittest.TestCase):
    def test_process_data(self):
        self.assertEqual(process_data("abc"), "ABC (admin)")
    def test_dummy_data(self):
        self.assertIsNotNone(get_db_data())


    