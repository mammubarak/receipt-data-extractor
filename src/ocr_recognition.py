import cv2
import pytesseract
import os

def ocr_recognition(image, output_folder, file_name):

    # Apply binary thresholding to make the text stand out
    _, thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)

    # Use pytesseract to extract text
    custom_config = r'--oem 3 --psm 6'  # Set OCR Engine mode and Page Segmentation mode
    text = pytesseract.image_to_string(thresh, config=custom_config)

    # Save the extracted text to a file
    save_text(output_folder, file_name, text)
    print(f"Extracted text from {file_name}:")
    print(text)
    return text

def save_text(output_folder, file_name, text):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    text_file_path = os.path.join(output_folder, f"{file_name}.txt")

    with open(text_file_path, "w") as text_file:
        text_file.write(text)
    print(f"|__Text saved to {text_file_path}.")