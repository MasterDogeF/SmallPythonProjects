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
while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower, upper = get_limits(colour)

    mask = cv2.inRange(hsvImage, lower, upper)
    mask_ = Image.fromarray(mask)

    countours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #returns 2 values but we only need 1, hence the _

    for object in countours:
        if cv2.contourArea(object) > 400:
            x, y, w, h = cv2.boundingRect(object) #x, y represent the top-left corner
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) #adding width and height gives the bottom-right cornet

    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()