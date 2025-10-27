import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load the image in grayscale
image_path = 'moon.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded properly
if image is None:
    print("Error: Unable to load image")
    exit()

# Apply Laplacian filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Convert to 8-bit image
laplacian_8bit = cv2.convertScaleAbs(laplacian)

# Sharpen the image by adding the Laplacian result to the original
sharpened_image = cv2.addWeighted(image, 1.5, laplacian_8bit, -0.5, 0)

# Display the results using matplotlib
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Laplacian ')
plt.imshow(laplacian_8bit, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Sharpened Image  ')
plt.imshow(sharpened_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()