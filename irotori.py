#coding: utf-8

import cv2
import numpy as np

roi_eyes = cv2.imread('pokari1.jpg', cv2.IMREAD_COLOR)
roi_nose = cv2.imread('pokari2.jpg', cv2.IMREAD_COLOR)
roi_mouth = cv2.imread('pokari3.jpg', cv2.IMREAD_COLOR)

spring = 0
summer = 0
autumn = 0
winter = 0

def season(roi_parts):
    hue = 0
    saturation = 0
    value = 0

    global spring
    global summer
    global autumn
    global winter

    if roi_parts is False:
        no_parts = roi_parts


    #HSV空間に変換
    hsvcat = cv2.cvtColor(roi_parts, cv2.COLOR_BGR2HSV)

    #切り抜いた画像の中心点
    tyuusin = (hsvcat[hsvcat.shape[0]/2, hsvcat.shape[1]/2]),\
              (hsvcat[hsvcat.shape[0]/2+1, hsvcat.shape[1]/2+1]),\
              (hsvcat[hsvcat.shape[0]/2+1, hsvcat.shape[1]/2-1]),\
              (hsvcat[hsvcat.shape[0]/2-1, hsvcat.shape[1]/2+1]),\
              (hsvcat[hsvcat.shape[0]/2-1, hsvcat.shape[1]/2-1])

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
    elif ave_saturation < (255/2) and ave_value < (255/2):
        print '秋'
        autumn += 1
    elif ave_saturation < (255/2) and ave_value > (255/2):
        print '夏'
        summer += 1
    elif ave_saturation > (255/2) and ave_value < (255/2):
        print '冬'
        winter += 1

if type(roi_eyes) != bool:
    season(roi_eyes)
else:
    print('目の色判別してないよ')

if type(roi_nose) != bool:
    season(roi_nose)
else:
    print('鼻の色判別してないよ')

if type(roi_mouth) != bool:
    season(roi_mouth)
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

#import pdb; pdb.set_trace()
cv2.imshow('roi_mouth',roi_mouth)
cv2.waitKey()


