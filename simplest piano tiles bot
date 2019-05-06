import pyautogui
import time
from mss import mss
import keyboard

start_x = 610 # starting position of leftmost tile
start_y = 600 # middle of leftmost tile

cords_x = [0, 140, 280, 420] # coordinates of each tile

bbox = (start_x, start_y, start_x + 500, start_y + 1)


# for coordinates

# def print_mouse_pos():
#     while True:
#         print(pyautogui.position())
#         time.sleep(1)
#
#print_mouse_pos()

def start():
    with mss() as sct:
        while True:
            img = sct.grab(bbox)
            for cord in cords_x:
                if img.pixel(cord, 0)[0] < 80:
                    pyautogui.click(start_x + cord, start_y)

            try:
                if keyboard.is_pressed('q'): # for exiting
                    break
                else:
                    pass
            finally:
                pass

time.sleep(5) # to have 5 secs before starting the game
start()
