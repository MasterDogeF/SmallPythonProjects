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

ball_pos = [wCam/2, hCam/2]
ball_radius = 30
gravity = 0.5
ball_vel = [5,0]
fingerVelocities = [None,None]*4
fingerOldPositions = [None,None]*4
framesToSpeedCheck = 5
frames = 0

score = 0

def ball_collision(ball_pos, ball_vel, radius, p1, p2, handID):
    bx, by = ball_pos
    vx, vy = ball_vel
    x1, y1 = p1
    x2, y2 = p2

    # Segment vector
    sx = x2 - x1
    sy = y2 - y1
    seg_len_sqr = sx * sx + sy * sy

    # If thumb & index are on top of each other, skip
    if seg_len_sqr == 0:
        return ball_pos, ball_vel, False
    
    # Project ball centre onto the line, get closest point on the segment
    t = ((bx - x1) * sx + (by - y1) * sy) / seg_len_sqr
    t = max(0.0, min(1.0, t))

    cx = x1 + t * sx
    cy = y1 + t * sy

    # Vector from closest point to ball centre
    dx = bx - cx
    dy = by - cy
    dist_sqr = dx * dx + dy * dy

    # Check if within the radius

    ball_speed = math.hypot(ball_vel[0], ball_vel[1])
    finger_speed = fingerVelocities[handID] / 5 if fingerVelocities[handID] is not None else 1

    collision_radius = radius + 0.05 * finger_speed + 0.03 * ball_speed
    collision_radius = max(radius, min(collision_radius, radius * 3))
    
    if dist_sqr > collision_radius * collision_radius:
        return ball_pos, ball_vel, False

    #normal (direction from paddle -> ball)
    dist = math.sqrt(dist_sqr) if dist_sqr != 0 else 1.0
    nx = dx / dist
    ny = dy / dist

    #only bounce if ball is moving towards the paddle
    #if vx * nx + vy * ny >= 0:
        #return ball_pos, ball_vel, False

    # Reflect velocity across normal
    dot = vx * nx + vy * ny
    rvx = vx - 2 * dot * nx * 1.1
    rvy = vy - 2 * dot * ny * 1.1

    # Push the ball out to the surface so it doesn't get stuck
    bx = cx + nx * radius 
    by = cy + ny * radius 

    return [bx, by], [rvx, rvy], True

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    fingers = [None,None]*4
    bases = [None,None]*4
    lines = [[None, None],[None, None]]*4

    ball_vel[1] += gravity   

    old_pos = ball_pos.copy()
    dx, dy = ball_vel

    dist = math.hypot(dx,dy)
    max_step = 10.0
    steps = max(1, int(dist / max_step))
    print(steps)

    collided = False
    for i in range(steps):
        ball_pos[0] = old_pos[0] + dx * (i+1) / steps
        ball_pos[1] = old_pos[1] + dy * (i+1) / steps

        if ball_pos[0] > wCam or ball_pos[0] < 0 or ball_pos[1] > hCam+300 or ball_pos[1] < 0:
            cv2.putText(frame, 'you lost!', (int(wCam/2), int(hCam/2)), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 15, cv2.LINE_AA)
            break
        
        if results.multi_hand_landmarks:
            for handID, handLms in enumerate(results.multi_hand_landmarks):
                for id, lm in enumerate(handLms.landmark):
                    h,w,c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    if id == 4:
                        cv2.circle(frame, (cx,cy), 10, (255,255,255), cv2.FILLED)
                        bases[handID] = (cx,cy)
                    if id == 8:
                        cv2.circle(frame, (cx,cy), 10, (255,255,255), cv2.FILLED)
                        fingers[handID] = (cx,cy)
                        if fingerOldPositions[handID] is None:
                            fingerOldPositions[handID] = fingers[handID]

                if fingers[handID] != None and bases[handID] is not None:
                    lines[handID] = [bases[handID], fingers[handID]]
                    cv2.line(frame, bases[handID], fingers[handID], (255,100,0), 15)
                
                if fingers[handID] is not None and bases[handID] is not None:
                    ball_pos, ball_vel, hit = ball_collision(ball_pos, ball_vel, ball_radius, lines[handID][0], lines[handID][1], handID)
                    if hit:
                        score += 1
                        collided = True
                        break

                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

        if collided:
            break

    if frames >= framesToSpeedCheck:
        for i in range(len(fingers)):
            if fingers[i] is not None and fingerOldPositions[i] is not None:
                fingerVelocities[i] = math.dist(fingerOldPositions[i] , fingers[i])
                fingerOldPositions[i] = fingers[i]
                frames = 0
    else:
        frames += 1

    cv2.circle(frame, (int(ball_pos[0]), int(ball_pos[1])), ball_radius, (255,255,255), cv2.FILLED)
    cv2.putText(frame, f"score: {score}", (5,100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5, cv2.LINE_AA)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("r"):
        ball_pos = [wCam/2, hCam/2]
        ball_vel = [5,0]
        score = 0

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break