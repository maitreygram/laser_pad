import cv2
import numpy as np
import math
image = cv2.imread('dot.png', 0)
Gray_Threshold = 127
print('Shape = ',image.shape)
print(image[1][1])
mean  = 0
for i in range (0, image.shape[0]):
	for j in range (0, image.shape[1]):	
		mean += image[i][j]

mean = mean/(image.size)
Standard_deviation = 0
for i in range (0, image.shape[0]):
	for j in range (0, image.shape[1]):	
		 Standard_deviation +=  math.pow((image[i][j] - mean), 2)
Standard_deviation = math.pow(Standard_deviation/(image.size), 0.5)
print ('mean = ',mean)
print ('Standard_deviation', Standard_deviation)
ret,thresh_img = cv2.threshold(image, Gray_Threshold, 255, cv2.THRESH_BINARY)
cv2.imwrite('binary_image.png', thresh_img)
