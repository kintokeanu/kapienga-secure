import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpg")

# Apply the Gaussian blur filter
kernel_size = (5, 5)
image_blurred = cv2.GaussianBlur(image, kernel_size, 0)

# Show the original and blurred images
cv2.imshow("Original", image)
cv2.imshow("Blurred", image_blurred)
cv2.waitKey(0)
