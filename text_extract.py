import cv2
import pytesseract
import os

# Telling Python where to find Pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# print current woring directory
my_folder = os.listdir()
print(my_folder)

# Filtering out images only
my_images = []  # Data to be extracted
for file in my_folder:
    # print(file)
    if file.endswith("png"):
        my_images.append(file)
print(my_images)


# Read Image using open cv
def my_reader():
    for image in my_images:
        # Read image with openCV
        read_image = cv2.imread(image)
        # Extract text using tesseract engine
        text = pytesseract.image_to_string(read_image)

        # create a new file and write our extracted text
        my_extract = open("my_extract.txt", "a+")
        my_extract.write(text)

        # close the file
        my_extract.close()
    return "Done Sir! It was Fun"


print(my_reader())
