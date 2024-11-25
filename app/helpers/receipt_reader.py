import os
from app.helpers.json_converter import convert_to_json
from app.helpers.db import get_from_db, save_to_db
import base64
import uuid

from openai import OpenAI

# Path to your images
images_directory = os.path.join(os.getcwd(), "images")

client = OpenAI()

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def read_receipt(image_path):
    # Generate the corresponding JSON file name
    receipt_file_name = os.path.basename(image_path) + '.json'
    db_path = os.path.join(os.getcwd(), 'db', receipt_file_name)

    # Check if the result already exists in the database
    if os.path.exists(db_path):
        # If the file exists, return the cached data
        return get_from_db(receipt_file_name)
    
    # If not, process the image, convert the receipt and save the result
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Read the image and return the detail",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
    )
    receipt_detail = response.choices[0].message.content
    result = convert_to_json(receipt_detail=receipt_detail)
    
    # Save the result with the corresponding file name
    result["file_name"] = receipt_file_name;
    result['id'] = str( uuid.uuid4());

    
    # Save the result to the database (db directory)
    save_to_db(result, receipt_file_name)
    
    return result

def get_result():
    responses = []
    for root, dir, files in os.walk(images_directory):
        for file in files:
            # Full path of the image
            image_path = os.path.join(images_directory, file)

            # Process each image and add its result
            receipt_result = read_receipt(image_path)
            
            # Add the file_name as part of the result
            result_with_filename = receipt_result
            result_with_filename["file_name"] = f"{file}.json"  # Attach the file name for storage

            responses.append(result_with_filename)
    return responses