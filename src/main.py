import cv2
import numpy as np
import sys
import os
import json


def display_and_save(title, image, step):
   """
   Display the image in a window and save it to disk.
   """
   cv2.imshow(title, image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   # Save the image with the step number
   cv2.imwrite(f'step_{step}_{title}.png', image)
   print(f"{title} image saved as step_{step}_{title}.png")

def save_extracted_text_to_file(bounding_boxes, image, text_filename):


def main(image_path):
    # Check if the image exists
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        sys.exit(1)

    print("Step 1: Loading the image.")
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image.")
        sys.exit(1)
    display_and_save("original", image, 1)

    print("Step 2: Converting to grayscale.")
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_and_save("grayscale", gray, 2)

    print("Step 3: Applying Gaussian Blur to reduce noise.")
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    display_and_save("blurred", blurred, 3)

    print("Step 4: Performing Canny edge detection.")
    # Perform Canny edge detection
    # edged = cv2.Canny(gray, 25, 450)
    edged = cv2.Canny(gray, 50, 250, apertureSize = 5, L2gradient = True)
    display_and_save("canny", edged, 4)

    print("Step 5: Applying dilation to connect text regions.")
    # Apply dilation to connect text regions
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilated = cv2.dilate(edged, kernel, iterations=1)
    display_and_save("dilated", dilated, 5)

    print("Step 6: Finding contours in the image.")
    # Find contours
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print(f"Step 7: Filtering contours based on size and aspect ratio. Total contours found: {len(contours)}")
    # Initialize list to hold bounding boxes
    bounding_boxes = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        area = w * h
        # Filter based on aspect ratio and area
        if 0.2 < aspect_ratio < 5 and area > 100:
            bounding_boxes.append((x, y, w, h))

    print(f"Step 8: Number of text regions detected: {len(bounding_boxes)}")
   # Draw bounding boxes on the original image
    output_image = image.copy()
    for bbox in bounding_boxes:
       x, y, w, h = bbox
       cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
       display_and_save("detected_text", output_image, 8)

    print("Step 9: Saving detected text regions to JSON.")
   # Save detected text regions to a JSON file
    save_detected_text_to_json(bounding_boxes, 'detected_text_regions.json')

    

    print("Text detection and extraction completed successfully.")




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python text_detector.py <path_to_image>")
        sys.exit(1)
    image_path = sys.argv[1]
    main(image_path)
