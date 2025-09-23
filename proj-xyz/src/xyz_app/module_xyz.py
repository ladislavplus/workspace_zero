"""Main application functions with dotenv support."""
from dotenv import load_dotenv
from glob_utils.helpers import get_text_dummy
import os

load_dotenv()  # Loads variables from .env

def process_xyz_data(data):
    """Process input data and return result."""
    db_user = os.getenv("DB_USER", "default_user")
    return f"{data.upper()} ({db_user})"

def get_x_text(str):
    if not str:
        return None 
    return "xyz.. " + get_text_dummy(str)

if __name__ == "__main__":
    print(get_x_text("RRR"))