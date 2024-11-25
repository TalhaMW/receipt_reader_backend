import os

class Config:
    INPUT_DIR = os.path.join(os.getcwd(), "images")
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
    # OUTPUT_DIR = os.path.join(os.getcwd(), "images", "output")

# Example: Load this in __init__.py with `app.config.from_object(Config)`


# print(Config.INPUT_DIR)
