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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python text_detector.py <path_to_image>")
        sys.exit(1)
    image_path = sys.argv[1]
    main(image_path)
