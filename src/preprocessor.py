import cv2
import os

def resize_image(image, output_folder, file_name):
    # Minimum dimensions (width, height) for resizing small images
    min_width, min_height = 800, 1200
    height, width = image.shape[:2]
    print(f"Original image dimensions: height: {height}, width: {width}")

    # Resize if the image is smaller than the minimum width/height
    if width < min_width or height < min_height:
        scale_factor = max(min_width / width, min_height / height)
        new_dimensions = (int(width * scale_factor), int(height * scale_factor))
        resized_image = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_AREA)

        # Save resized image
        save_image(resized_image, output_folder, f"resized_{file_name}")
        print(f"Image resized to {new_dimensions}.")
        return resized_image
    else:
        print("Image size is sufficient, no resizing needed.")
        return image

def save_image(image, output_folder, file_name):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, file_name)
    cv2.imwrite(output_path, image)