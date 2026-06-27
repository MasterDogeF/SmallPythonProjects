import pyautogui
import random

import time
time.sleep(0.2)

pyautogui.PAUSE = 0

#beg 1010 393 9 9, int 983 393 16 16, 

top_left_x = 983
top_left_y = 393
tile_size = 50
rows = 16
columns = 16

Board = []

class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.number = -1 #-1 = unknown, 0 = empty
        self.isMine = False

def reset():
    pyautogui.leftClick(1234, 306)

def click_random_tile():
    random_x = top_left_x + (tile_size * random.randint(1,rows-1))
    random_y = top_left_y + (tile_size * random.randint(1,columns-1))

    click_x = random_x + tile_size//2
    click_y = random_y + tile_size//2

    pyautogui.leftClick(click_x, click_y)
    update_board()

def click_tile(tile):
    click_x = top_left_x + (tile_size * tile.x) + tile_size//2
    click_y = top_left_y + (tile_size * tile.y) + tile_size//2

    pyautogui.leftClick(click_x, click_y)
    time.sleep(0.005)
    update_board()

def flag_tile(tile):
    click_x = top_left_x + (tile_size * tile.x) + tile_size//2
    click_y = top_left_y + (tile_size * tile.y) + tile_size//2

    pyautogui.rightClick(click_x, click_y)
    tile.isMine = True
    time.sleep(0.005)
    update_board()

def print_board():
    for y in range(columns):
        for x in range(rows):
            print(Board[y][x].number, end="")
        print()

def update_board():
    img = pyautogui.screenshot()
    for y in range(columns):
        for x in range(rows):
            if not Board[y][x].isMine:
                pixel_x = top_left_x + (tile_size * x) + tile_size//2 + 4 #31
                pixel_y = top_left_y + (tile_size * y) + tile_size//2 #38
                match img.getpixel((pixel_x, pixel_y)):
                    case (124, 199, 255):
                        Board[y][x].number = 1
                    case (102, 194, 102):
                        Board[y][x].number = 2
                    case (255, 119, 136):
                        Board[y][x].number = 3
                    case (238, 136, 255):
                        Board[y][x].number = 4
                    case (221, 170, 34):
                        Board[y][x].number = 5
                    case (102, 204, 204):
                        Board[y][x].number = 6
                    case (153, 153, 153):
                        Board[y][x].number = 7
                    case (208, 216, 224):
                        Board[y][x].number = 8
                    case (56, 64, 72):
                        Board[y][x].number = 0
                    case _:
                        Board[y][x].number = -1

def get_near_mines(tile):
    moves = [[0,1], [-1,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0]]
    mines = []
    unrevealed = []
    for i in range(8):
        neighbor_y = tile.y + moves[i][1]
        neighbor_x = tile.x + moves[i][0]
        if neighbor_y >= 0 and neighbor_y < rows and neighbor_x >= 0 and neighbor_x < columns:
            neighbor = Board[neighbor_y][neighbor_x]
            if neighbor.isMine:
                mines.append(neighbor)
            elif neighbor.number == -1 and not neighbor.isMine:
                unrevealed.append(neighbor)
    return mines, unrevealed
    


Board = [[Tile(x, y) for x in range(rows)] for y in range(columns)]
update_board()
print_board()

click_random_tile()

start_time = time.time()
while time.time() - start_time < 20:
    action_found = False
    for y in range(columns):
        for x in range(rows):
            tile = Board[y][x]
            if not tile.isMine and tile.number > 0:
                mines, unrevealed = get_near_mines(tile)
                if len(unrevealed) > 0:
                    if tile.number - len(mines) == len(unrevealed):
                        for unrevealedTile in unrevealed:
                            action_found = True
                            flag_tile(unrevealedTile)
                    elif tile.number == len(mines):
                        action_found = True
                        click_tile(tile)
                time.sleep(0.005)
    if not action_found:
        click_random_tile()
    if pyautogui.pixel(1394, 320) == (0,0,0):
        reset()
        Board = [[Tile(x, y) for x in range(rows)] for y in range(columns)]
        time.sleep(0.1)
        update_board()

while True:
    x, y = pyautogui.position()
    #print(f"\rX:{x} Y:{y}", end="")
    #print(pyautogui.pixel(x, y))
    


