import argparse
import os
from src.image_reader import read_image
from src.preprocessor import resize_image, grayscale_image, deskew_image

def main():
    # Set up CLI argument parsing
    parser = argparse.ArgumentParser(description="Receipt Processing CLI")
    parser.add_argument("image_path", type=str, help="Path to the receipt image")
    parser.add_argument("--compare", action="store_true", help="Compare multiple receipts")

    args = parser.parse_args()
    file_name = os.path.basename(args.image_path)

    text_output_folder = "data/summaries/"
    image_output_folder = "images/processed/"
    comparison_output_folder = "data/comparison/"
    
    if args.compare:
        # Compare multiple receipts
        compare_receipts(text_output_folder, comparison_output_folder)
    else:
        # Call the image reading function
        image = read_image(args.image_path)
        if image is not None:
            # Step 1: Resize the image if needed
            print("Step 1: Resizing image...")
            image = resize_image(image, image_output_folder, file_name)

            # Step 2: Convert the image to grayscale
            print("Step 2: Converting image to grayscale...")
            image = grayscale_image(image, image_output_folder, file_name)

            # Step 3: Deskew the image to correct angle
            print("\nStep 3: Deskew image to correct angles...")
            #image = deskew_image(image, image_output_folder, file_name)

            # Step 4: Smooth folds
            print("Step 4: Smoothing folds...")
            image = smooth_folds(image, image_output_folder, file_name)


if __name__ == "__main__":
    main()