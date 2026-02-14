import pygame
import random
import json

background_colour = (10,10,10)
(width, height) = (1280, 720)

pygame.init()

timer = pygame.time.Clock()

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Engine')

font = pygame.font.Font('freesansbold.ttf', 32)
dialogueTxt = font.render('', True, 'white')
nameTxt = font.render('', True, 'white')
count = 0
textRect = dialogueTxt.get_rect()
nameRect = nameTxt.get_rect()
textRect.center = (0 + (width // 3), height - (height // 8))
nameRect.center = (0 + (width // 3), height - (height // 5.5))

dialogue_bg = pygame.Surface((width, height), pygame.SRCALPHA)

def getScenes():
    with open("Scenes.json") as file:
        return json.load(file)

def clear():
    display.fill(background_colour)

def multi_line_text(text):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            display.blit(font.render(l, True, 'White'), (textRect.x, textRect.y + font.get_linesize()*i))

Scenes = getScenes()
currentScene = Scenes["intro"]
textIndex = 0
awaitingInput = False
charbodys = []


running = True
while running:
    clear() 

    currentTexts = currentScene["text"]
    speed = currentScene["speed"]
    bg = currentScene["bg"]

    text = currentTexts[textIndex]

    timer.tick(60)

    #bg
    img = pygame.image.load(bg+".png").convert()
    img = pygame.transform.scale(img, (width, height))
    display.blit(img, (0,0))

    if text[0] == "char+": 
        charbodys.append(text[1])
        textIndex += 1
        text = currentTexts[textIndex]
    elif text[0] == "char-":
        charbodys.remove(text[1])
        textIndex += 1
        text = currentTexts[textIndex]

    for char in charbodys: #character bodys
        img = pygame.image.load(char[0].lower()+"full.png").convert_alpha()
        img = pygame.transform.scale(img, ((width / 3.88)*1.75, (height / 1.3)*1.75))
        x, y = 0, height // 16
        match char[1]:
            case "centre":
                rect = img.get_rect(midtop=(width // 2, y))
        display.blit(img, rect)
    
    pygame.draw.rect(dialogue_bg, (69, 69, 69, 120), (width//3.5, 0, width, height//3.5)) #dialogue box
    display.blit(dialogue_bg, (0, height-(height // 3.5)))

    dialogueTxt = font.render(text[1][0:count], True, 'white')
    nameTxt = font.render(text[0], True, 'white')

    multi_line_text(text[1][0:count])
    display.blit(nameTxt, nameRect)

    if text[0] != "": #character head
        charfound = False
        for char in charbodys:
            if char[0] == text[0].lower():
                charfound = True
                
        if not charfound:
            img = pygame.image.load(text[0].lower()+".png").convert_alpha()
            img = pygame.transform.scale(img, (width // 3, height // 2))
            display.blit(img, (0, height - (height // 2)))
        
    if count < len(text[1]):
        awaitingInput = False
        count += 1
    else:
        awaitingInput = True


    pygame.display.flip()

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN and awaitingInput:
            count = 0
            textIndex += 1
            if textIndex >= len(currentTexts):
                currentScene = Scenes[currentScene["next"]]
                charbodys = []
                textIndex = 0