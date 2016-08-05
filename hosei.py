#coding: utf-8

import cv2
import numpy as np

img = cv2.imread('koka.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#lower_red = np.array([0, 50, 50])
#upper_red = np.array([2 ,255, 255])

lower_red2 = np.array([175, 50, 50])
upper_red2 = np.array([180,255, 255])

img_mask = cv2.inRange(hsv, lower_red2, upper_red2)

color_mask = cv2.bitwise_and(img, img, mask=img_mask)
gray_mask = cv2.cvtColor(color_mask, cv2.COLOR_BGR2GRAY)
img_color = cv2.split(color_mask)

b_sum = 0
g_sum = 0
r_sum = 0

for x in img_color[0]:
    for y in x:
        b_sum += y

for x in img_color[1]:
    for y in x:
        g_sum += y

for x in img_color[2]:
    for y in x:
        r_sum += y

count = cv2.countNonZero(gray_mask)
ave_blue = b_sum/count
ave_green = g_sum/count
ave_red= r_sum/count

change_blue = 22-ave_blue
change_green= 28-ave_green
change_red= 237-ave_red


for w in img:
    for h in w:
        if h[0].astype(np.float64)+change_blue > 255:
            h[0] = 255
        else:
            h[0] += change_blue

        if h[1].astype(np.float64)+change_green > 255:
            h[1] = 255
        else:
            h[1] += change_green
            
        if h[2].astype(np.float64)+change_red > 255:
            h[2] = 255
        else:
            h[2] += change_red
        
print ave_blue, ave_green, ave_red
print change_blue, change_green, change_red

#import pdb; pdb.set_trace()
cv2.imshow('img',img)
#cv2.imshow('re_img',re_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
