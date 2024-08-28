##Log Transformation
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('dft.png')
c= 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log ( 1 + img)
log_transformed = np.array(log_transformed, dtype = np.uint8)

plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Origianl'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(log_transformed, cmap = 'gray')
plt.title ('Transform'), plt.xticks([]), plt.yticks([])

plt.show()