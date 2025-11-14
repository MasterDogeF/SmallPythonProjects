import cv2
import mediapipe as mp
import random
import math

wCam, hCam = 1280, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

maxTargets = 10
targets = []

while True:
    ret, frame = cap.read()
    imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    #create array of fingers
    fingers = [(-999,-999),(-999,-999)]

    if len(targets) < maxTargets:
        x = random.randint(0,wCam)
        y = random.randint(0,hCam)
        targets.append((x,y))
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h,w,c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    cv2.circle(frame, (cx,cy), 15, (255,255,0), cv2.FILLED)
                    if fingers[0] == (-999, -999):
                        fingers[0] = (cx,cy)
                    else:
                        fingers[1] = (cx,cy)

            mpDraw.draw_landmarks(frame, handLms)
    
    new_targets = []
    for target in targets:
        if fingers[0] != (-999,-999) or fingers[1] != (-999,-999):
            finger1X = fingers[0][0]
            finger1Y = fingers[0][1]
            finger2X = fingers[1][0]
            finger2Y = fingers[1][1]
            if math.dist([finger1X,finger1Y], [target[0], target[1]]) < 40 or math.dist([finger2X,finger2Y], [target[0], target[1]]) < 40:
                continue

        cv2.circle(frame, target, 40, (0,0,255), 5)
        new_targets.append((target[0], target[1]))

    targets = new_targets

    cv2.imshow("frame",cv2.flip(frame,1))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break