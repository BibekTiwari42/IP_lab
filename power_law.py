##Power Law Transform
import cv2
import numpy as np
from matplotlib import pyplot as plt
img_1 = cv2. imread("star.jpg",0)
gamma = 2
img_2 = np.power(img_1, gamma)
gamma =1.5
img_3 = np.power(img_1, gamma)
gamma = 1
img_4 = np.power(img_1 , gamma)
gamma = 2.5

plt.subplot(221)
plt.imshow(img_1, cmap="gray")
plt.title("original")
plt.xticks([]), plt.yticks([])

plt.subplot(222)
plt.imshow(img_2, cmap="gray")
plt.title("Gamma-2")
plt.xticks([]), plt.yticks([])

plt.subplot(223)
plt.imshow(img_3, cmap="gray")
plt.title("Gamma-3")
plt.xticks([]), plt.yticks([])

plt.subplot(224)
plt.imshow(img_4, cmap="gray")
plt.title("Gamma-4")
plt.xticks([]), plt.yticks([])

plt.show()
