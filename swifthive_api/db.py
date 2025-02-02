from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()  # Load environment variables from .env file

DB_URL = os.getenv('DB_URL')
print(DB_URL)  # Print DB_URL to verify it's loaded correctly

if DB_URL:  # Only create engine if DB_URL is valid
    engine = create_engine(DB_URL)
else:
    print("DB_URL is not set properly.")
