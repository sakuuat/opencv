#coding: utf-8

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose')

hue = 0
saturation = 0
value = 0


img = cv2.imread('lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, 1.1, 3)

#切り抜いて格納
for (x,y,w,h) in face:

    roi_gray = gray[y:y+h, x:x+w]
    roi_face = img[y:y+h, x:x+w]

    #HSV空間に変換
hsvcat_face = cv2.cvtColor(roi_face, cv2.COLOR_BGR2HSV)

    #切り抜いた画像の中心点
tyuusin = (hsvcat_face[hsvcat_face.shape[0]/2, hsvcat_face.shape[1]/2]),\
(hsvcat_face[hsvcat_face.shape[0]/2+1, hsvcat_face.shape[1]/2+1]),\
(hsvcat_face[hsvcat_face.shape[0]/2+1, hsvcat_face.shape[1]/2-1]),\
(hsvcat_face[hsvcat_face.shape[0]/2-1, hsvcat_face.shape[1]/2+1]),\
(hsvcat_face[hsvcat_face.shape[0]/2-1, hsvcat_face.shape[1]/2-1])

#import pdb; pdb.set_trace()

for h,s,v in tyuusin:
    hue += h.astype(np.float64)
    saturation += s.astype(np.float64)
    value += v.astype(np.float64)

ave_hue = hue/5
ave_saturation = saturation/5
ave_value = value/5


#彩度と明度の判定
if ave_saturation > (255/2) and ave_value > (255/2):
    print '春'
elif ave_saturation < (255/2) and ave_value < (255/2):
    print '秋'
elif ave_saturation < (255/2) and ave_value > (255/2):
    print '夏'
elif ave_saturation > (255/2) and ave_value < (255/2):
    print '冬'

print 'H=',ave_hue,  'S=',ave_saturation,  'V=',ave_value

#cv2.imshow('detected.jpg', hsvcat_face)
#cv2.waitKey()

