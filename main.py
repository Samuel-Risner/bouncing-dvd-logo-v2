from tkinter import Tk, PhotoImage, Canvas
from time import sleep
from threading import Thread

WINDOW_WIDTH = 380
WINDOW_HEIGHT = 190
    
root = Tk()
root.overrideredirect(True)
root.config(bg="blue", bd=0, highlightthickness=0)
root.attributes("-transparentcolor", "blue")
root.attributes("-topmost", True)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")

canvas = Canvas(root, bg="blue", bd=0, highlightthickness=0)
canvas.pack()

img = PhotoImage(file="img.png")
img = img.subsample(13)
canvas.create_image(0, 0, image=img, anchor="nw")

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

def threder():
    max_x = SCREEN_WIDTH - WINDOW_WIDTH
    max_y = SCREEN_HEIGHT - WINDOW_HEIGHT

    dir_x = 1
    dir_y = -1

    x = 0
    y = 0

    run = True
    while run:
        new_x = x + (1 * dir_x)
        new_y = y + (1 * dir_y)

        if new_y < 0:
            new_y = 0
            dir_y = dir_y * -1
        elif y > max_y:
            new_y = max_y
            dir_y = dir_y * -1

        if new_x < 0:
            new_x = 0
            dir_x = dir_x * -1
        elif x > max_x:
            new_x = max_x
            dir_x = dir_x * -1

        x = new_x
        y = new_y

        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
        
        sleep(0.001)


th = Thread(target=threder)
th.start()

root.mainloop()