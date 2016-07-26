#coding: utf-8

import cv2
import numpy as np

img = cv2.imread('koka.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#lower_red = np.array([0, 50, 50])
#upper_red = np.array([2 ,255, 255])

lower_red2 = np.array([175, 50, 50])
upper_red2 = np.array([180,255, 255])

#img_mask = cv2.inRange(hsv, lower_red, upper_red)
img_mask = cv2.inRange(hsv, lower_red2, upper_red2)

color_mask = cv2.bitwise_and(hsv, hsv, mask=img_mask)
gray_mask = cv2.cvtColor(color_mask, cv2.COLOR_BGR2GRAY)
img_color = cv2.split(color_mask)

h_sum = 0
s_sum = 0
v_sum = 0

for x in img_color[0]:
    for y in x:
        h_sum += y

for x in img_color[1]:
    for y in x:
        s_sum += y

for x in img_color[2]:
    for y in x:
        v_sum += y

#count = len(np.where(gray_mask!=0)[2])
count = cv2.countNonZero(gray_mask)
ave_hue = h_sum/count
ave_saturation = s_sum/count
ave_value = v_sum/count

print h_sum, s_sum, v_sum
print "count=", count
print ave_hue, ave_saturation, ave_value


#import pdb; pdb.set_trace()
cv2.imshow('img',color_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
