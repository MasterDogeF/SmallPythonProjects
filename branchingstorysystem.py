import json 
import time
from rich.console import Console


def getScenes():
    with open("Scenes.json") as file:
        return json.load(file)

def PrintLine(text, speed):
    currentStyle = ""
    loadingStyle = False
    for i in range(len(text)):
        if loadingStyle:
            currentStyle = currentStyle + text[i]
            if text[i] == "]":
                if text[i-1] == "/":
                    currentStyle = ""
                loadingStyle = False
        else:
            if text[i] == "[":
                loadingStyle = True
                currentStyle = currentStyle + text[i]
            else:
                if i < len(text) - 1:
                    Console().print(currentStyle+text[i], end="")
                else:   
                    Console().print(currentStyle+text[i], end="\n")
                time.sleep(0.05/speed)

def answer(prompt, valid):
    while True:
        try:
            value = int(input(prompt))
            if value in valid: return value
        except ValueError:
            pass
        print("Please type a valid number:", valid)

def run():
    Scenes = getScenes()
    currentScene = Scenes["intro"]
    speed = currentScene["speed"]

    while True:
        if currentScene.get("title"):
            PrintLine(currentScene["title"],0.35)
        
        for text in currentScene["text"]:
            PrintLine(text, speed)
            time.sleep(1 / speed)

        print("")

        choices = currentScene.get("choices")
        if choices:
            for choice in choices:
                PrintLine(choice["text"], speed)
        
            Answer = answer("Enter your choice: ", range(1,len(choices)+1))
            currentScene = Scenes[choices[Answer-1]["next"]]

run()

