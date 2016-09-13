#coding: utf-8

import cv2
import numpy as np

img = cv2.imread('pokari.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([100, 50, 50])
upper_red = np.array([120 ,255, 255])

img_mask = cv2.inRange(hsv, lower_red, upper_red)
color_mask = cv2.bitwise_and(hsv, hsv, mask=img_mask)
gray_mask = cv2.cvtColor(color_mask, cv2.COLOR_BGR2GRAY)
img_color = cv2.split(color_mask)

s_sum = 0
v_sum = 0

for x in img_color[1]:
    for y in x:
        s_sum += y

for x in img_color[2]:
    for y in x:
        v_sum += y

count = cv2.countNonZero(gray_mask)
ave_saturation = s_sum/count
ave_value = v_sum/count

change_saturation = 186-ave_saturation
change_value = 190-ave_value

for w in img:
    for h in w:

        if h[1].astype(np.float64)+change_saturation > 255:
            h[1] =255 
        else:
            h[1] += change_saturation

        if h[2].astype(np.float64)+change_value > 255:
            h[2] = 255 
        else:
            h[2] += change_value


re_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
print ave_saturation, ave_value
print change_saturation, change_value

#import pdb; pdb.set_trace()
cv2.imshow('img',img)
cv2.imshow('re_img',re_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
