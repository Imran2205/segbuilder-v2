import json
from pathlib import Path
from werkzeug.security import generate_password_hash

from ..config import LOCAL_FOLDER, LOCAL_DB_FILE

# Local JSON and filesystem storage for this single-user application.


def initialize_local_data():
    """Create the local storage directory and database on first launch."""
    Path(LOCAL_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(LOCAL_DB_FILE).parent.mkdir(parents=True, exist_ok=True)

    if not Path(LOCAL_DB_FILE).exists():
        initial_data = {
            "users": {
                "local_user": {"password": generate_password_hash("password")}
            },
            "projects": {"local_user": {"projects": []}},
            "project-classes": {},
            "sessions": {},
        }
        save_local_db(initial_data)

def get_local_folder():
    """
    Ensure the local folder exists and return its path.

    This function checks if the local folder exists, and if not, creates it.

    :return: The path to the local folder.
    """
    Path(LOCAL_FOLDER).mkdir(parents=True, exist_ok=True)
    return str(LOCAL_FOLDER)

def get_local_db():
    """
    Load the local database from a JSON file.

    This function checks if the local database file exists. If not, it creates
    an empty JSON file. It then reads and returns the contents of the file.

    :return: The contents of the local database as a dictionary.
    """
    initialize_local_data()
    with open(LOCAL_DB_FILE, 'r') as f:
        return json.load(f)

def save_local_db(data):
    """
    Save data to the local database JSON file.

    This function writes the provided data to the local database file in JSON format.

    :param data: The data to save to the local database.
    """
    with open(LOCAL_DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)
