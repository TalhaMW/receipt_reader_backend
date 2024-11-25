

import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import pyheif
import os  # Importing the os module to handle file operations

# def heic_to_jpg(heic_path):
#     try:
#         # Read the .HEIC file
#         heif_file = pyheif.read(heic_path)
#         image = Image.frombytes(
#             heif_file.mode,
#             heif_file.size,
#             heif_file.data,
#             "raw",
#             heif_file.mode,
#             heif_file.stride,
#         )
#         # Replace .HEIC extension with .jpg
#         jpg_path = heic_path.replace(".HEIC", ".jpg")
#         # Save the image as a .jpg file
#         image.save(jpg_path, "JPEG")
#         # Delete the original .HEIC file
#         os.remove(heic_path)
#         print(f"Converted {heic_path} to {jpg_path} and deleted the original .HEIC file.")
#         return jpg_path
#     except FileNotFoundError:
#         print(f"Error: File {heic_path} not found.")
#     except Exception as e:
#         print(f"An unexpected error occurred while converting {heic_path}: {e}")

# def image_reader():
#     try:
#         # Load the image file using PIL
#         img = Image.open('test_1_img.png')
#         # Run OCR on the image
#         text = pytesseract.image_to_string(img)
#         print(text)
#     except FileNotFoundError:
#         print("Error: 'test_1_img.png' not found. Please check the file path.")
#     except pytesseract.TesseractNotFoundError:
#         print("Error: Tesseract is not installed or not in PATH.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Example usage:
# # heic_to_jpg('example.HEIC')
# image_reader()


import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import pyheif
import os  # Importing the os module to handle file operations

def heic_to_jpg(heic_path):
    text_array = heic_path.split(".");
    # print("<><><><><><><><><><><><><> ",text_array," <><><><><><><><>")
    text_ext = text_array[len(text_array)-1];
    # print(text_ext);
    
    if(text_ext=="HEIC"):
        try:
            # Read the .HEIC file
            heif_file = pyheif.read(heic_path)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            # Replace .HEIC extension with .jpg
            jpg_path = heic_path.replace(".HEIC", ".jpg")
            # Save the image as a .jpg file
            image.save(jpg_path, "JPEG")
            # Delete the original .HEIC file
            os.remove(heic_path)
            # print(f"Converted {heic_path} to {jpg_path} and deleted the original .HEIC file.")
            return jpg_path
        except FileNotFoundError:
            print(f"Error: File {heic_path} not found.")
        except Exception as e:
            print(f"An unexpected error occurred while converting {heic_path}: {e}")
    else:
        return 1









def pdf_to_text(pdf_path):
    
    text_array = pdf_path.split(".");
    # print("<><><><><><><><><><><><><> ",text_array," <><><><><><><><>")
    text_ext = text_array[len(text_array)-1];
    print(text_ext);
    
    if(text_ext=='jpg' or text_ext=='png' or text_ext=='HEIC'):
        if(text_ext=='HEIC'):
            print("run")
            img = heic_to_jpg(pdf_path)
            result = pytesseract.image_to_string(img);
            print(result)
            return 1
        else:
            print("run")
            result = pytesseract.image_to_string(pdf_path);
            print(result)
            return 1


# pdf_to_text("IMG_6102.jpg")


import os 
images_directory = os.path.join(os.getcwd(),"images");
print( images_directory );


for root,dir,files in os.walk( images_directory):
    for file in files:
        heic_to_jpg(images_directory+"/"+file)