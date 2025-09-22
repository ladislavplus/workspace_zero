"""Main application functions with dotenv support."""
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env

def process_abc_data(data):
    """Process input data and return result."""
    db_user = os.getenv("DB_USER", "default_user")
    return f"{data.upper()} ({db_user})"
