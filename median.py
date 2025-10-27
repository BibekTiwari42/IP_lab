import cv2
import numpy as np
from matplotlib import pyplot as plt
img= cv2.imread ('boys.png')
blur1 = cv2.medianBlur(img,5)
blur2= cv2.medianBlur(img,7)
blur3= cv2.medianBlur(img,9)
plt.subplot (221), plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur1), plt.title('Blurred1')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(blur2), plt.title('Blurred2')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(blur3), plt.title('Blurred3')
plt.xticks([]), plt.yticks([])
plt.show()
