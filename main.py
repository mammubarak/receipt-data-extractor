import argparse
import os
from src.image_reader import read_image
from src.preprocessor import resize_image, grayscale_image, smooth_folds, deskew_image
from src.text_detection import detect_text_areas
from src.ocr_recognition import ocr_recognition
from src.summarizer import summarize_receipt
from src.visualizer import compare_receipts

def main():
    # Set up CLI argument parsing
    parser = argparse.ArgumentParser(description="Receipt Processing CLI")
    parser.add_argument("image_path", type=str, nargs="?", help="Path to the receipt image")
    parser.add_argument("--compare", action="store_true", help="Compare multiple receipts")

    args = parser.parse_args()
    file_name = None

    text_output_folder = "data/summaries/"
    image_output_folder = "images/processed/"
    comparison_output_folder = "data/comparison/"
    
    if args.compare:
        # Compare multiple receipts
        compare_receipts(text_output_folder, comparison_output_folder)
    else:
        file_name = os.path.basename(args.image_path)
        # Call the image reading function
        image = read_image(args.image_path)
        if image is not None:
            # Step 1: Resize the image if needed
            print("\nStep 1: Resizing image...")
            image = resize_image(image, image_output_folder, file_name)

            # Step 2: Convert the image to grayscale
            print("\nStep 2: Converting image to grayscale...")
            image = grayscale_image(image, image_output_folder, file_name)

            # Step 3: Deskew the image to correct angle
            print("\nStep 3: Deskew image to correct angles...")
            # image = deskew_image(image, image_output_folder, file_name)

            # Step 4: Smooth folds
            print("\nStep 4: Smoothing folds...")
            image = smooth_folds(image, image_output_folder, file_name)

            # Step 5: Detect text areas
            print("\nStep 5: Detecting text areas in the image...")
            # image = detect_text_areas(image, image_output_folder, file_name)

            # Step 6: Perform OCR to extract text
            print("\nStep 6: Extrating text from image using OCR...")
            extracted_text = ocr_recognition(image, text_output_folder, file_name)

            # Step 7: Summarize the receipt
            print("\nStep 7: Summarizing the receipt...")
            summarize_receipt(extracted_text, text_output_folder, file_name)

if __name__ == "__main__":
    main()