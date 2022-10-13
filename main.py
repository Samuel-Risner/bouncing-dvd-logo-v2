from tkinter import Tk, PhotoImage, Canvas
from threading import Thread
import time, random

WINDOW_WIDTH = 375
WINDOW_HEIGHT = 175
IMG_POS_X = 0
IMG_POS_Y = 0
SUBSAMPLE_VALUE = 13

MAX_SPEED = 10
MIN_SPEED = 5
SPEED = [int(MAX_SPEED / 2), int(MAX_SPEED / 2)]
    
root = Tk()
root.overrideredirect(True)
# root.config(bg="white", bd=0, highlightthickness=0)
root.attributes("-transparentcolor", "white")
root.attributes("-topmost", True)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")

canvas = Canvas(root, bg="white", bd=0, highlightthickness=0)
canvas.pack()

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

def change_colour():
    while True:
        for _ in range(0, 19, 1):
            yield False

        yield True

def next_image():
    images = list()

    def add_img(colour_matching:str, file:int):
        f = f"images/{colour_matching}_png/{colour_matching}{file}.png"
        img = PhotoImage(file=f)
        img = img.subsample(SUBSAMPLE_VALUE)
        images.append(img)

    for i in range(1, 12, 1):
        add_img("bg", i)

    for i in range(11, 0, -1):
        add_img("gb", i)

    for i in range(1, 12, 1):
        add_img("gr", i)

    for i in range(11, 0, -1):
        add_img("rg", i)

    for i in range(1, 12, 1):
        add_img("rb", i)

    for i in range(11, 0, -1):
        add_img("br", i)

    while True:
        for img in images:
            yield img

def change_speed():
    SPEED[0] = random.randint(MIN_SPEED, MAX_SPEED - 1)
    SPEED[1] = MAX_SPEED - SPEED[0]     

CHANGE_COLOUR_GENERATOR = change_colour()
GET_NEXT_IMAGE = next_image()

def threder():
    max_x = SCREEN_WIDTH - WINDOW_WIDTH
    max_y = SCREEN_HEIGHT - WINDOW_HEIGHT

    dir_x = 1
    dir_y = 1

    x = 0
    y = 0

    run = True
    while run:
        new_x = x + SPEED[0] * dir_x
        new_y = y + SPEED[1] * dir_y

        if new_y < 0:
            new_y = 0
            dir_y = dir_y * -1
            change_speed()
        elif y > max_y:
            new_y = max_y
            dir_y = dir_y * -1
            change_speed()

        if new_x < 0:
            new_x = 0
            dir_x = dir_x * -1
            change_speed()
        elif x > max_x:
            new_x = max_x
            dir_x = dir_x * -1
            change_speed()

        x = new_x
        y = new_y

        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
        
        time.sleep(0.005)

        if next(CHANGE_COLOUR_GENERATOR):
            root.attributes("-topmost", True)
            canvas.create_image(IMG_POS_X, IMG_POS_Y, image=next(GET_NEXT_IMAGE), anchor="nw")

th = Thread(target=threder)
th.start()

root.mainloop()