import cv2
import numpy
from PIL import Image

def get_limits(colour):
    c = numpy.uint8([[colour]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) 

    hue = hsvC[0][0][0] #hue value
    
    if hue >= 165: #if at the top range only get the last 10 colour range
        lower = numpy.array([hue - 10, 100, 100], dtype=numpy.uint8) 
        upper = numpy.array([179, 255, 255], dtype=numpy.uint8)
    elif hue <= 15: #if at the bottom range only get the first 10 colour range
        lower = numpy.array([0, 100, 100], dtype=numpy.uint8)
        upper = numpy.array([hue + 10, 255, 255], dtype=numpy.uint8)
    else:
        lower = numpy.array([hue - 10, 100, 100], dtype=numpy.uint8)
        upper = numpy.array([hue + 10, 255, 255], dtype=numpy.uint8)

    return lower,upper

colour = [0,255,255] #BGR format
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    faceX1, faceY1, faceX2, faceY2 = 0,0,0,0

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.05, 6) #1.05=scale factor (higher values give faster performance), 6=accuracy
    for (x, y, w, h) in faces:
        faceX1 = x-75
        faceY1 = y+150
        faceX2 = x+w+75
        faceY2 = y+h+200
        cv2.rectangle(frame, (faceX1,faceY1), (faceX2, faceY2), (255,0,0), 4)


    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower, upper = get_limits(colour)

    mask = cv2.inRange(hsvImage, lower, upper)

    countours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #returns 2 values but we only need 1, hence the _

    detected = False
    for object in countours:
        if cv2.contourArea(object) > 400:
            x, y, w, h = cv2.boundingRect(object)   
            centreX = x + w/2
            centreY = y + h/2

            if (faceX1 <= centreX <= faceX2 and faceY1 <= centreY <= faceY2) and h>w:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) #x, y represent the top-left corner #adding width and height gives the bottom-right cornet
                cv2.putText(frame, 'Landyard detected', (faceX1-25, faceY1-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                detected = True
    
    if not detected:
        cv2.putText(frame, 'no lanyard, execution on 15/11/2025', (faceX1-30, faceY1-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 200), 2, cv2.LINE_AA)


    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()