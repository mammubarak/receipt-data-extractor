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



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python text_detector.py <path_to_image>")
        sys.exit(1)
    image_path = sys.argv[1]
    main(image_path)
