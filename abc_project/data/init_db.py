"""Setup database and insert test data with dotenv support."""
from dotenv import load_dotenv
import os
import sys
from abcapp.module_app import process_abc_data

load_dotenv()  # Loads variables from .env

def setup_db():
    db_host = os.getenv("DB_HOST", "localhost")
    print(f'Database initialized at {db_host}.')

def insert_test_data():
    sample = process_abc_data('test')
    print(f'Inserted: {sample}')

if __name__ == '__main__':
    # Add PYTHONPATH from .env to sys.path
    # project_root = os.getenv("PYTHONPATH")
    # if project_root and project_root not in sys.path:
      #  sys.path.append(project_root)

    setup_db()
    insert_test_data()

