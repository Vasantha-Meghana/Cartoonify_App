# cartoonify_utils.py

import cv2
import numpy as np

def cartoonify_image(image):
    # Convert image to RGB format (OpenCV loads images in BGR)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert to grayscale
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # Apply median blur to reduce noise
    smooth = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(smooth, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to smoothen colors but preserve edges
    color = cv2.bilateralFilter(img_rgb, 9, 300, 300)

    # Combine edge mask with color image for cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon
