import cv2
import os


def read_image(image_path):
    try:
        # Check if the file exists
        if not os.path.exists(image_path):
            print(f"File not found: {image_path}")
            return None

        # Read the image using OpenCV
        image = cv2.imread(image_path)

  # Check if the file is corrupted
        if image is None:
            print(f"Image could not be read. The file might be corrupted or not a valid image.")
            return None
        return image
    except Exception as e:
        print(f"Error reading the image: {e}")
        return None
    
    