# data-scraper-project/database/initialize_db.py

import sys
from pathlib import Path

# Add the parent directory to sys.path to be able to import from the database package
current_path = Path(__file__).resolve()
root_path = current_path.parent.parent
sys.path.append(str(root_path))

from database.db_manager import initialize_database

def initialize_data():
    print("Initializing the database and creating tables...")
    initialize_database()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_data()
