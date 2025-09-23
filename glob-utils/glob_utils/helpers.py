from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env


def calculate_dummy(value):
    return value * 2

def get_text_dummy(str):
    return str + "dummy added."

def get_global_text():
    txt = os.getenv("ENVVAR")
    return txt
