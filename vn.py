import pygame
import random
import json
import asyncio

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
textRect.center = (0 + (width // 3), height - (height // 5.5))
nameRect.center = (0 + (width // 3), height - (height // 4.5))

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
type_timer = 0.0

running = True
while running:
    clear() 

    currentTexts = currentScene["text"]
    speed = currentScene["speed"]
    bg = currentScene["bg"]

    text = currentTexts[textIndex]
    
    dt = timer.tick(60)
    ms_per_char = 50 / speed
    print(dt)

    #bg
    img = pygame.image.load(bg+".png").convert()
    img = pygame.transform.scale(img, (width, height))
    display.blit(img, (0,0))

    if text[0] == "char+": 
        charbodys.append(text[1])
        textIndex += 1
        count = 0
        type_timer = 0.0
        continue
    elif text[0] == "char-":
        for char in charbodys:
            if char["name"] == text[1]:
                char["fading"] = "out"
        textIndex += 1
        count = 0
        type_timer = 0.0
        continue
    
    for char in charbodys:
        if char["fading"].lower() == "in":
            if char["alpha"] >= 255:
                char["fading"] == "none"
            else:
                char["alpha"] += dt / 1.25
        elif char["fading"].lower() == "out":
            if char["alpha"] <= 0:
                char["fading"] == "none"
                charbodys.remove(char)
            else:
                char["alpha"] -= dt / 1.25
    
        img = pygame.image.load(char["name"].lower()+"full.png").convert_alpha()
        img = pygame.transform.scale(img, ((width / 3.88)*1.75, (height / 1.3)*1.75))
        x, y = 0, height // 16
        match char["pos"]:
            case "centre":
                rect = img.get_rect(midtop=(width // 2, y))
        img.set_alpha(char["alpha"])
        display.blit(img, rect)

    dialoguebox = pygame.image.load("dialoguebox.png").convert_alpha()
    dialoguebox = pygame.transform.scale(dialoguebox, (width//1.4, height//3.5))
    dialoguebox.set_alpha(169)
    display.blit(dialoguebox, (width-(width//1.4), height-(height // 3.5)))

    #pygame.draw.rect(dialogue_bg, (69, 69, 69, 120), (width//3.5, 0, width, height//3.5)) #dialogue box
    #display.blit(dialogue_bg, (0, height-(height // 3.5)))

    dialogueTxt = font.render(text[1][0:count], True, 'white')
    nameTxt = font.render(text[0], True, 'white')

    display.blit(nameTxt, nameRect)

    if text[0] != "": #character head
        charfound = False
        for char in charbodys:
            if char["name"] == text[0].lower():
                charfound = True
                
        if not charfound:
            img = pygame.image.load(text[0].lower()+".png").convert_alpha()
            img = pygame.transform.scale(img, (width // 3, height // 2))
            display.blit(img, (0, height - (height // 2)))
        
    if count < len(text[1]):
        awaitingInput = False
        type_timer += dt
        while type_timer >= ms_per_char and count < len(text[1]):
            count += 1
            type_timer -= ms_per_char
    else:
        awaitingInput = True

    multi_line_text(text[1][0:count])

    pygame.display.flip()

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if awaitingInput:
                count = 0
                textIndex += 1
                type_timer = 0.0
                if textIndex >= len(currentTexts):
                    currentScene = Scenes[currentScene["next"]]
                    charbodys = []
                    textIndex = 0
            else:
                count = len(text[1])