import cv2
import mediapipe as mp
import pyautogui
import random
import math

wCam, hCam = 1280, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
        
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            fingers = []
            yCheckFinger = (None,None)
            for id, lm in enumerate(handLms.landmark):
                h,w,c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id in [8,12,16,20]:
                    fingers.append(cy)
                elif id == 13:
                    yCheckFinger = cy

            open = False
            for finger in fingers:
                if finger < yCheckFinger - 30:
                    open = True
                    break
            if open:
                pyautogui.mouseUp(button='left')
            else:
                pyautogui.mouseDown(button='left')
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break