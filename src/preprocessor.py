import cv2
import os

def save_image(image, output_folder, file_name):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, file_name)
    cv2.imwrite(output_path, image)
    print(f"|__ Image saved to {output_path}.")