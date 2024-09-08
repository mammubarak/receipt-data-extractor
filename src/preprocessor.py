import cv2
import os

def resize_image(image, output_folder, file_name):
    # Minimum dimensions (width, height) for resizing small images
    min_width, min_height = 800, 1200
    height, width = image.shape[:2]
    print(f"|__ Original image dimensions: height: {height}, width: {width}")

    # Resize if the image is smaller than the minimum width/height
    if width < min_width or height < min_height:
        scale_factor = max(min_width / width, min_height / height)
        new_dimensions = (int(width * scale_factor), int(height * scale_factor))
        resized_image = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_AREA)

        # Save resized image
        save_image(resized_image, output_folder, f"resized_{file_name}")
        print(f"|__ Image resized to {new_dimensions}.")
        return resized_image
    else:
        print("|__ Image size is sufficient, no resizing needed.")
        return image

def grayscale_image(image, output_folder, file_name):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def deskew_image(image, output_folder, file_name):

    # Use Gaussian blur to remove noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply edge detection or binary thresholding to highlight contours
    edged = cv2.Canny(blurred, 50, 150)

    # Find the contours of the edges
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If contours are found, proceed with finding the angle
    if len(contours) > 0:
        # Get the largest contour (likely the receipt boundary)
        largest_contour = max(contours, key=cv2.contourArea)

        # Get the minimum bounding box for the contour
        rect = cv2.minAreaRect(largest_contour)

        # Get the angle of rotation
        angle = rect[-1]

        # The angle may sometimes be negative, adjust it
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle

        # Rotate the image to deskew
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        deskewed_image = cv2.warpAffine(image, rotation_matrix, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

        # Save the deskewed image
        save_image(deskewed_image, output_folder, f"deskewed_{file_name}")
        print(f"|__ Image deskewed by {angle} degrees.")
        return deskewed_image
    else:
        print("|__ No contours found for deskewing.")
        return image

def smooth_folds(image, output_folder, file_name):
    # Apply Gaussian blur to smooth out folds and wrinkles
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Save blurred image
    save_image(blurred_image, output_folder, f"smoothed_{file_name}")
    print("|__ Image smoothed to reduce folds.")
    return blurred_image

def save_image(image, output_folder, file_name):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, file_name)
    cv2.imwrite(output_path, image)
    print(f"|__ Image saved to {output_path}.")