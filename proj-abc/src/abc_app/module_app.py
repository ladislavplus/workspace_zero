"""Main application functions with dotenv support."""
from dotenv import load_dotenv
import os
import logging
from glob_utils.helpers import calculate_dummy, get_global_text

load_dotenv()  # Loads variables from .env

# --- Logging setup --- main setup, just once
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def process_abc_data(data):
    """Process input data and return result."""
    db_user = os.getenv("DB_USER", "default_user")
    logging.info(f"Processing data: {data}")
    return f"{data.upper()} ({db_user})"


if __name__ == "__main__":
    print(process_abc_data("DATA001"))
    print(get_global_text())
    print(calculate_dummy(2))

    