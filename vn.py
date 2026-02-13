import pygame
import random
import json

background_colour = (10,10,10)
foreground_colour = (0,0,0)
(width, height) = (800, 500)

pygame.init()

timer = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)
txt = font.render('', True, foreground_colour)
count = 0
textRect = txt.get_rect()
textRect.center = (width // 2, height // 1.2)

display = pygame.display.set_mode((width, height))

pygame.display.set_caption('Engine')

def getScenes():
    with open("Scenes.json") as file:
        return json.load(file)

def clear():
    display.fill(background_colour)

running = True
while running:
    clear()
    
    timer.tick(60)

    pygame.draw.rect(display, 'gray', [0, 300, 800, 200])

    Scenes = getScenes()
    currentScene = Scenes["sleep"]
    currentTexts = currentScene["text"]
    speed = currentScene["speed"]

    text = ""

    txt = font.render(text[0:count//speed], True, foreground_colour)
    display.blit(txt, textRect)

    if count < speed*len(text):
        count += 1
    else:
        count = 0

    pygame.display.flip()

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False