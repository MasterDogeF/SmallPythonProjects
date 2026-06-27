import pyautogui
import pytesseract
import random
import time
import cv2
import numpy as np
time.sleep(0.2)

pyautogui.PAUSE = 0

#beg 1010 393 9 9, int 983 393 16 16, 

top_left_x = 804
top_left_y = 208
tile_size = 55

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

templates = {}

for i in range(1, 10):
    templates[i] = cv2.imread(
        f"numbers/{i}.png",
        cv2.IMREAD_GRAYSCALE
    )

Board = []

Board = [[0 for x in range(9)] for y in range(9)]

def read_board():
    for y in range(9):
        for x in range(9):
            cell_x = top_left_x + (tile_size * x)
            cell_y = top_left_y + (tile_size * y)
            img = pyautogui.screenshot(None, (cell_x+4, cell_y+4, tile_size-4, tile_size-4))
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

            best_number = 0
            best_score = -1

            for number, template in templates.items():
                result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

                score = result.max()

                if score > best_score:
                    best_score = score
                    best_number = number

            if best_score < 0.5:
                best_number = 0

            Board[y][x] = best_number

def print_board():
    for y in range(9):
        for x in range(9):
            print(Board[y][x], end="")
        print()


def solve(x,y):
    if y == 9:
        return True
    elif x == 9:
        return solve(0,y+1)
    elif Board[y][x] != 0:
        return solve(x+1,y)
    else:
        for i in range(1,10):
            if is_valid(x,y,i):
                Board[y][x] = i
                if solve(x+1,y):
                    return True
                else:
                    Board[y][x] = 0
        return False

def is_valid(x,y,num):
    if num in Board[y]:
        return False
    for i in range(9):
        if Board[i][x] == num:
            return False
    for i in range((y//3)*3, (y//3)*3+3):
        for j in range((x//3*3), (x//3*3+3)):
            if Board[i][j] == num:
                return False
    return True


def input_answer():
    for y in range(9):
        for x in range(9):
            click_x = top_left_x + (tile_size * x) + tile_size//2
            click_y = top_left_y + (tile_size * y) + tile_size//2
            pyautogui.leftClick(click_x, click_y)
            match Board[y][x]:
                case 1:
                    pyautogui.leftClick(1376, 382)
                case 2:
                    pyautogui.leftClick(1483, 382)
                case 3:
                    pyautogui.leftClick(1590, 382)
                case 4:
                    pyautogui.leftClick(1376, 487)
                case 5:
                    pyautogui.leftClick(1483, 487)
                case 6:
                    pyautogui.leftClick(1590, 487)
                case 7:
                    pyautogui.leftClick(1376, 582)
                case 8:
                    pyautogui.leftClick(1483, 582)
                case 9:
                    pyautogui.leftClick(1590, 582)
            
read_board()
#print_board()

solve(0,0)
#print_board()
input_answer()

while True:
    x, y = pyautogui.position()
    print(f"\rX:{x} Y:{y}", end="")
    #print(pyautogui.pixel(x, y))