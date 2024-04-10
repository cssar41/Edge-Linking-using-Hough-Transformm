# In[ ]:## Read image and convert it to grayscale image
## Developed by : Abishek Xavier A
## Reg no : 212222230004
import cv2
import numpy as np
import matplotlib.pyplot as plt
image1=cv2.imread('eren.png',0)
img= cv2.GaussianBlur()
plt.imshow(img)

## Find the edges in the image using canny detector and display
## Developed by : Abishek Xavier A
## Reg no : 212222230004
edges1 = cv2.Canny(img,)
plt.imshow(edges1,cmap = 'gray')
plt.title('Edge Image'), plt.xticks()
plt.show()

## Detect points that form a line using HoughLinesP
## Developed by : Abishek Xavier A
## Reg no : 212222230004
lines=cv2.HoughLinesP(edges1,1,np.pi/180, threshold=80, minLineLength=50,maxLineGap=250)

## Draw lines on the image
## Developed by : Abishek Xavier A
## Reg no : 212222230004
for line in lines:
    x1, y1, x2, y2 = line [0] 
    cv2.line(edges1,(x1, y1),,3)



## Display the result
## Developed by : Abishek Xavier A
## Reg no : 212222230004
plt.imshow(edges1)

