import argparse
import os


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
    

if __name__ == "__main__":
    main()