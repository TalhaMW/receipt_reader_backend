import os
import json

DB_DIRECTORY = os.path.join(os.getcwd(), 'db')

# Function to save data to a JSON file (acting as a simple DB)
def save_to_db(data, file_name):    
    # Construct file path
    file_path = os.path.join(DB_DIRECTORY, file_name)
    
    # Write the data to a JSON file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to fetch data from the "database"
def get_from_db(file_name):
    file_path = os.path.join(DB_DIRECTORY, file_name)
    
    # Check if the file exists and return the parsed JSON data
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        return None  # Return None if the file does not exist
