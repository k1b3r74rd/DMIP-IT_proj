import keyboard, os, time, threading
from SI_Project.sheet import sheet
import SI_Project.action

A = []

protagonist_y = 13
protagonist_x = 9
score = 0

projectile_y = 12
projectile_x = 9
projectile_type = " | "



def greetings():
    def start(enter):
        if enter.name == "enter":
            sheet(projectile_y, projectile_x, projectile_type)

    os.system('cls')
    print('Welcome to da game. Press "Enter" to start da game.')
    keyboard.hook(start)


if __name__ == "__main__":
    greetings()
    while True:
        keyboard.hook(protagonist_movement)
        keyboard.wait()
