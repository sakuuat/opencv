#coding: utf-8

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('image3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, 1.1, 3)

#切り抜いて格納
for (x,y,w,h) in face:
    cat_face = img[y:y+h, x:x+w]

    #HSV空間に変換
    hsvcat_face = cv2.cvtColor(cat_face, cv2.COLOR_BGR2HSV)

    #切り抜いた画像の中心点
    tyuusin = hsvcat_face[hsvcat_face.shape[0]/2, hsvcat_face.shape[1]/2]

    #彩度と明度の判定
    if tyuusin[1] > (255/2) and tyuusin[2] > (255/2):
        print '春', tyuusin[1], tyuusin[2]
    elif tyuusin[1] < (255/2) and tyuusin[2] < (255/2):
        print '秋', tyuusin[1], tyuusin[2]
    elif tyuusin[1] < (255/2) and tyuusin[2] > (255/2):
        print '夏', tyuusin[1], tyuusin[2]
    elif tyuusin[1] > (255/2) and tyuusin[2] < (255/2):
        print '冬', tyuusin[1], tyuusin[2]


#cv2.imshow('detected.jpg', hsvcat_face)
#cv2.waitKey()

