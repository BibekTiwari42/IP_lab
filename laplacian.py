import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('white.webp')
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
img_hpf = cv2.filter2D(image, -1, kernel)
# Convert images from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_hpf_rgb = cv2.cvtColor(img_hpf, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(image_rgb), plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_hpf_rgb), plt.title('Laplacian Filter Applied')
plt.xticks([]), plt.yticks([])
plt.show()
