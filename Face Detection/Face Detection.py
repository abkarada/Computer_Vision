import cv2 as cv

face_cascade = cv.CascadeClassifier('C:/Users/ASUS/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

camera = cv.VideoCapture(0)

if not camera.isOpened():
    exit()

while True:
    _, img = camera.read()

    if img is None:
        break
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    cv.imshow("Face Detection", img)

    if cv.waitKey(5) == ord('x'):
        break    

camera.release()

cv.destroyAllWindows()

'''to find harsh paths use 
import cv2 as cv
import os

# OpenCV'nin veri yolunu al
haar_cascade_path = cv.data.haarcascades

# Haar kaskad yüz tanıma dosyasının tam yolunu yazdır
print(os.path.join(haar_cascade_path, 'haarcascade_frontalface_default.xml'))

'''