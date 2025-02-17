# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 02:07:25 2025

@author: Ryuzaki
"""

import cv2

# HOG sınıflandırıcısını yükle (insan tespiti için)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    exit()

while True:
    ret, img = camera.read()
    
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8), padding=(8, 8), scale=1.05)

    count = 0
    for (x, y, w, h) in boxes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, f"People count: {count}", (10, 30), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("People Counting", img)

    if cv2.waitKey(1) == ord('x'):
        break

camera.release()

cv2.destroyAllWindows()
