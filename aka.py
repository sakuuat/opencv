import cv2
import numpy as np

img = cv2.imread('koka.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 50, 50])
upper_red = np.array([5 ,255, 255])

lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180,255, 255])

img_mask = cv2.inRange(hsv, lower_red, upper_red)
img_mask += cv2.inRange(hsv, lower_red2, upper_red2)


img_color = cv2.bitwise_and(img, img, mask=img_mask)


#import pdb; pdb.set_trace()

cv2.imshow('img',img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
