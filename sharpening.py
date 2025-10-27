import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("white.webp",cv2.COLOR_BGR2GRAY)
gauss_mask = cv2.GaussianBlur(image, (9,9),10.0)
image_sharp = cv2.addWeighted(image, 2, gauss_mask, -1, 0)
kernel = np.array([[-1, -1, -1],
                  [-1, 8, -1],
                  [-1, -1, -1]])
image_hpf = cv2.filter2D(image, -1, kernel)
plt.figure(figsize=(10,8))
plt.subplot(3,2,1)
plt.title('orignial Image')
plt.imshow (image, cmap='gray')
plt.axis('off')
plt.subplot(3,2,2)
plt.title('Sharpenign Filter')
plt.imshow(image_sharp, cmap='gray')
plt.axis('off')
plt.subplot(3,2,3)
plt.title('High Pass Filter')
plt.imshow(image_hpf, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()