import os
from app.helpers.receipt_reader import get_result
from app.helpers.db import save_to_db

# Path to the DB directory
DB_DIRECTORY = os.path.join(os.getcwd(), 'db')

# Ensure the db directory exists
os.makedirs(DB_DIRECTORY, exist_ok=True)

def process_images():
    # Get results (which includes file names for each processed image)
    result = get_result()

    # Save each result to the "database" with corresponding file name
    for res in result:
        # For each processed result, derive the file name (e.g., IMG_6237.jpg.json)
        file_name = res.get("file_name", "default.json")  # Use a default name if no file name exists
        save_to_db(res, file_name)
    
    return {"status": "success", "processed_images": result}
