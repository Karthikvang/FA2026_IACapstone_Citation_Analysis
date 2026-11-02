"""Loads API keys from the .env file. Import from here instead of pasting keys into code.

    from config import API_KEY, API_EMAIL
"""
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_EMAIL = os.getenv("API_EMAIL")

if not API_KEY:
    raise RuntimeError("API_KEY is missing. Copy .env.example to .env and fill it in (see README).")
