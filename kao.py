#coding: utf-8

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_mcs_righteye.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth')

spring = 0
summer = 0
autumn = 0
winter = 0

img = cv2.imread('satomi1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray)

#切り抜いて格納
for (x,y,w,h) in face:
    roi_gray = gray[y:y+h, x:x+w]
    roi_face = img[y:y+h, x:x+w]
    cv2.rectangle(roi_face,(x,y),(x+w,y+h),(255,255,255),2)

#ここを調整したら正確性が上がる！
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
    nose = nose_cascade.detectMultiScale(roi_gray)
    mouth = mouth_cascade.detectMultiScale(roi_gray)
    

    if type(eyes) is tuple:
        roi_eyes = False
    else:
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_face,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            roi_eyes = roi_gray[y:y+h, x:x+w]

    if type(nose) is tuple: 
        roi_nose = False
    else:
        for (nx,ny,nw,nh) in nose:
            cv2.rectangle(roi_face,(nx,ny),(nx+nw,ny+nh),(255,0,0),2)
            roi_nose = roi_gray[y:y+h, x:x+w]

    if type(mouth) is tuple:
        roi_mouth = False 
    else:
        for (mx,my,mw,mh) in mouth:
            cv2.rectangle(roi_gray,(mx,my),(mx+mw,my+mh),(0,0,255),2)
            roi_mouth = roi_face[y:y+h, x:x+w]


def season(roi_parts, spring, summer, autumn, winter):

    hue = 0
    saturation = 0
    value = 0

    if roi_parts is False:
        no_parts = roi_parts

    import pdb; pdb.set_trace()

    #HSV空間に変換
    hsvcat = cv2.cvtColor(roi_parts, cv2.COLOR_BGR2HSV)

    #切り抜いた画像の中心点
    tyuusin = (hsvcat[hsvcat.shape[0]/2, hsvcat.shape[1]/2]),\
    (hsvcat[hsvcat.shape[0]/2+1, hsvcat.shape[1]/2+1]),\
    (hsvcat[hsvcat.shape[0]/2+1, hsvcat.shape[1]/2-1]),\
    (hsvcat[hsvcat.shape[0]/2-1, hsvcat.shape[1]/2+1]),\
    (hsvcat[hsvcat.shape[0]/2-1, hsvcat.shape[1]/2-1])


#    import pdb; pdb.set_trace()
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
        spring += 1
        return spring
    elif ave_saturation < (255/2) and ave_value < (255/2):
        print '秋'
        autumn += 1
        return autumn
    elif ave_saturation < (255/2) and ave_value > (255/2):
        print '夏'
        summer += 1
        return summer
    elif ave_saturation > (255/2) and ave_value < (255/2):
        print '冬'
        winter += 1
        return winter


if type(roi_face) != bool:
    season(roi_face, spring, summer, autumn, winter)
else:
    print('顔の色判別してないよ')

if type(roi_eyes) != bool:
    season(roi_eyes, spring, summer, autumn, winter)
else:
    print('目の色判別してないよ')

if type(roi_nose) != bool:
    season(roi_nose, spring, summer, autumn, winter)
else:
    print('鼻の色判別してないよ')

if type(roi_mouth) != bool:
    season(roi_mouth, spring, summer, autumn, winter)
else:
    print('口の色判別してないよ')


list = [spring, summer, autumn, winter]
re_season = max(list)

if re_season == spring:
    print'春が来た'
elif re_season == summer:
    print'夏が来た'
elif re_season == autumn:
    print'秋が来た'
elif re_season == winter:
    print'冬が来た'

#print 'H=',ave_hue,  'S=',ave_saturation,  'V=',ave_value


cv2.imshow('detected.jpg',img)
cv2.waitKey()

