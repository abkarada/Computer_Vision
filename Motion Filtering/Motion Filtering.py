# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 01:08:46 2025

@author: Ryuzaki
"""

import cv2 as cv

video = cv.VideoCapture(0)
subtractor = cv.createBackgroundSubtractorMOG2(0, 50)

while True:
    
    ret, frame = video.read()
    
    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

        if cv.waitKey(5) == ord('x'):
            break
    else:
        video = cv.VideoCapture(0)
        
cv.destroyAllWindows()
video.release()

