from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

class food:
    pass

class snake:
    pass

def next_turn():
    pass

def change_direction():
    pass

def check_collision():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score: " + str(score), font=("Arial", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# window_width = window.winfo_width() 
# window_height = window.winfo_height()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# x = int((screen_width / 2) - (window_width / 2))
# y = int((screen_height / 2) - (window_height / 2))

# window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# snake = Snake()
# food = Food()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = int((screen_width / 2) - (GAME_WIDTH / 2))
y = int((screen_height / 2) - (GAME_HEIGHT / 2))

window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}+{x}+{y}")


window.mainloop()
