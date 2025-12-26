import pygame
import time
import math

background_colour = (10,10,10)
foreground_colour = (0,255,0)
(width, height) = (800, 800)
FPS = 60

display = pygame.display.set_mode((width, height))

pygame.display.set_caption('3D Engine')


def clear():
    display.fill(background_colour)

def point(point):
    s = 20
    x = point[0]
    y = point[1]
    pygame.draw.rect(display, foreground_colour, (x-s/2, y-s/2, s, s))

def line(p1, p2):
    pygame.draw.line(display, foreground_colour, p1, p2)

def screen(point): #convert coordinate system from where 0 is centre to where 0 is top left
    x = point[0]
    y = point[1]
    # for x: [-1,1] -> [0,2] -> [0,1] -> [0,width]
    # for y: [-1,1] -> [0,2] -> [0,1] -> [1,0] -> [height,0]
    return ((x+1)/2*width, (1-(y+1)/2)*height) 

def project(point):
    x = point[0]
    y = point[1]
    z = point[2]

    return (x/z, y/z) #the magical formula for 3D projection

def translate(point, dx, dy, dz):
    x = point[0]
    y = point[1]
    z = point[2]
    return (x + dx, y + dy, z + dz)

def rotate_xz(point, angle):
    x = point[0]
    y = point[1]
    z = point[2]

    return ((x * math.cos(angle) - z * math.sin(angle), y, x * math.sin(angle) + z * math.cos(angle))) #rotate vector forumula

vertices = [
    (0.25, 0.25, 0.25),
    (-0.25, 0.25, 0.25),
    (-0.25, -0.25, 0.25),
    (0.25, -0.25, 0.25),

    (0.25, 0.25, -0.25),
    (-0.25, 0.25, -0.25),
    (-0.25, -0.25, -0.25),
    (0.25, -0.25, -0.25),
]

faces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7],
]


dz = 1
dx = 0.0
dy = 0.0
angle = 0

def frame():
    clear()
    #for vertex in vertices:
        #point(screen(project(translate(rotate_xz(vertex, angle), dx, dy, dz))))
    for face in faces:
        #connecting each contiguous vertex with a line 
        for i in range(0, len(face)):
            a = vertices[face[i]] #first vertex
            b = vertices[face[(i+1)%len(face)]] # wrap around

            line(
                screen(project(translate(rotate_xz(a, angle), dx, dy, dz))),
                screen(project(translate(rotate_xz(b, angle), dx, dy, dz)))
            )

    pygame.display.flip()

running = True
while running:
    delta = 1/FPS
    time.sleep(delta)

    angle += math.pi*delta
    frame()

    keys = pygame.key.get_pressed()
    speed = 1.0
    
    if keys[pygame.K_a]: dx += speed * delta
    if keys[pygame.K_d]: dx -= speed * delta

    if keys[pygame.K_s]: dz += speed * delta
    if keys[pygame.K_w]: dz -= speed * delta

    if keys[pygame.K_q]: dy += speed * delta
    if keys[pygame.K_e]: dy -= speed * delta

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                dx = 0
                dy = 0
                dz = 1
                angle = 0

            
