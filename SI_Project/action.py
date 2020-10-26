# Модуль, отвечающий за действия ГГ.

import os, time, keyboard, threading
from SI_Project.sheet import sheet, first_sheet

A = []

protagonist_y = 13
protagonist_x = 9
score = 0


# Функции, отвечающие за действия ГГ.
# Принимает и обрабатывает нажатие клавиш.
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
        shot()


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


# Функции, отвечающие за движение и поведение выстрела.
def projectile():
    global score
    global projectile_y, projectile_x, protagonist_y, protagonist_x
    projectile_y = protagonist_y
    projectile_x = protagonist_x

    def anima():
        global projectile_y, projectile_x, score
        j = False

        if A[projectile_y][projectile_x] == " | ":
            A[projectile_y][projectile_x] = "   "
        elif A[projectile_y][projectile_x] == "_|_":
            A[projectile_y][projectile_x] = "_ _"
        elif A[projectile_y][projectile_x] == " * " or A[projectile_y-1][projectile_x] == " * ":
            A[projectile_y][projectile_x] = '   '
            j = True

        if A[projectile_y - 1][projectile_x] == "   ":
            projectile_y -= 1
            A[projectile_y][projectile_x] = " | "

        elif A[projectile_y - 1][projectile_x] == "_ _":
            projectile_y -= 1
            A[projectile_y][projectile_x] = "_|_"
        else:
            projectile_y -= 1
            A[projectile_y][projectile_x] = " * "
            score += 100
            time.sleep(0.1)

        if projectile_y == 0 or j:
            A[projectile_y][projectile_x] = '   '
            j = False

        time.sleep(0.001)

    for i in range(13):
        sheet(anima())


def shot():
    global animation
    animation = threading.Thread(target=projectile)
    animation.start()
    # animation.join()
