##Hough Transform
import cv2 
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('suduko.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,250,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180, 200)   
for line in lines: 
   r,theta = line[0] 
   a = np.cos(theta) 
   b = np.sin(theta)
   x0 = a*r 
   y0 = b*r 
   x1 = int(x0 + 1000*(-b)) 
   y1 = int(y0 + 1000*(a))  
   x2 = int(x0 - 1000*(-b))  
   y2 = int(y0 - 1000*(a)) 
   img2=cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Original Image(Bibek)'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Hough Transform'),plt.xticks([]),plt.yticks([])
plt.show()