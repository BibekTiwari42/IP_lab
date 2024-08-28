## Image Segementation
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('cluster.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel=np.ones((5,5),np.uint8)
closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=2)

bg=cv2.dilate(closing,kernel,iterations=1)

dist_transform=cv2.distanceTransform(closing,cv2.DIST_L2,5)
ret,fg=cv2.threshold(dist_transform,0.3*dist_transform.max(),100,0)

plt.subplot(121),plt.imshow(img)
plt.title('Original Image(Bibek)'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(fg)
plt.title('Segmented Image(Bibek)'),plt.xticks([]),plt.yticks([])
plt.show()
