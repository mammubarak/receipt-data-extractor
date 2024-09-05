import cv2
import numpy as np
import os

def detect_text_areas(image, output_folder, file_name):
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(image)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if w > 20 and h > 20 and 0.1 < aspect_ratio < 10:
            cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), -1)
    detected_text_image = cv2.bitwise_and(image, mask)
    save_image(detected_text_image, output_folder, f"detected_text_{file_name}")
    return detected_text_image

def save_image(image, output_folder, file_name):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, file_name)
    cv2.imwrite(output_path, image)