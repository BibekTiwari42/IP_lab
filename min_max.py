import cv2
import numpy as np
import matplotlib.pyplot as plt
def min_filter(image, kernel_size):
    rows, cols = image.shape
    filtered_image = np.zeros((rows, cols), dtype=np.uint8)
    offset = kernel_size // 2
    padded_image = cv2.copyMakeBorder(image, offset, offset, offset, offset, cv2.BORDER_REFLECT)
    for i in range(offset, rows + offset):
        for j in range(offset, cols + offset):
            neighborhood = padded_image[i - offset:i + offset + 1, j - offset:j + offset + 1]
            min_value = np.min(neighborhood)
            filtered_image[i - offset, j - offset] = min_value
    
    return filtered_image

def max_filter(image, kernel_size):
    rows, cols = image.shape
    filtered_image = np.zeros((rows, cols), dtype=np.uint8)
    offset = kernel_size // 2
    padded_image = cv2.copyMakeBorder(image, offset, offset, offset, offset, cv2.BORDER_REFLECT)
    
    for i in range(offset, rows + offset):
        for j in range(offset, cols + offset):
            neighborhood = padded_image[i - offset:i + offset + 1, j - offset:j + offset + 1]
            max_value = np.max(neighborhood)
            filtered_image[i - offset, j - offset] = max_value
    
    return filtered_image

image = cv2.imread('noiseimg.jpeg', cv2.IMREAD_GRAYSCALE)
kernel_size = 3
min_filtered_image = min_filter(image, kernel_size)
max_filtered_image = max_filter(image, kernel_size)

plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image ')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(min_filtered_image, cmap='gray')
plt.title('Min Filtered Image ')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(max_filtered_image, cmap='gray')
plt.title('Max Filtered Image ')
plt.axis('off')

plt.show()