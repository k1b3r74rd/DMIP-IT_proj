# Модуль, отвечающий за действия ГГ.

import os, time, keyboard, threading
from SI_Project.sheet import sheet, first_sheet

A = []

protagonist_y = 13
protagonist_x = 9
score = 0


def action(button):
    global protagonist_x
    global protagonist_y
    if button.name == "left" and button.event_type == "down":
        if protagonist_x - 1 == 0:
            pass
        else:
            sheet(move_left())

    elif button.name == "right" and button.event_type == "down":
        if protagonist_x + 1 == 19:
            pass
        else:
            sheet(move_right())

    elif button.name == "space" and button.event_type == "down":
        sheet()


def move_left():
    global protagonist_y, protagonist_x
    A[protagonist_y][protagonist_x] = "   "
    protagonist_x -= 1
    A[protagonist_y][protagonist_x] = ' ^ '


def move_right():
    global protagonist_y, protagonist_x
    A[protagonist_y][protagonist_x] = "   "
    protagonist_x += 1
    A[protagonist_y][protagonist_x] = ' ^ '


def projectile():
    def kill(y, x):
        global score
        A[y][x] = " * "
        score += 100
        time.sleep(0.5)
        return ' * '

    global score
    projectile_y = protagonist_y
    projectile_x = protagonist_x
    for i in range(1, 13):
        if A[projectile_y][projectile_x] == " | ":
            A[projectile_y][projectile_x] = "   "
        elif A[projectile_y][projectile_x] == "_|_":
            A[projectile_y][projectile_x] = "_ _"
        elif A[projectile_y][projectile_x] == " * ":
            A[projectile_y][projectile_x] = "   "
            animation.join()
            break

        if A[projectile_y - 1][projectile_x] == "   ":
            projectile_y -= 1
            A[projectile_y][projectile_x] = " | "

        elif A[projectile_y - 1][projectile_x] == "_ _":
            projectile_y -= 1
            A[projectile_y][projectile_x] = "_|_"

        else:
            projectile_y -= 1
            A[projectile_y][projectile_x] = kill(projectile_y, projectile_x)

        time.sleep(0.05)


def shot():
    global animation
    animation = threading.Thread(target=projectile)
    animation.start()
