# Основной файл, из которого будет запускаться игра.

import keyboard, os, time, threading, multiprocessing
# from SI_Project.sheet import sheet, first_sheet
# import SI_Project.action

A = []
act = True

protagonist_y = 13
protagonist_x = 9
score = 0


def greetings():
    def start(enter):
        if enter.name == "enter":
            first_sheet()

    os.system('cls')
    print('Welcome to da game. Press "Enter" to start da game.')
    keyboard.hook(start)


# Основной декоратор для функций.
def sheet(function):
    global protagonist_y, protagonist_x, score, A
    os.system('cls')
    for i in range(0, 15):
        if i == 9:
            A.append(["_ _"] * 20)
        else:
            A.append(["   "] * 20)

    for i in range(1, 15):
        A[i][0] = "\ "
        A[i][19] = " /"

    func = function

    A[protagonist_y][protagonist_x] = ' ^ '
    A[0][0] = 'Score: ' + str(score)
    for i in range(15):
        print()
        for j in range(20):
            print(A[i][j], end="")
    print()


# Функция для первого вывода "поля боя".
def first_sheet():
    global protagonist_y, protagonist_x, score, A
    os.system('cls')
    for i in range(0, 15):
        if i == 9:
            A.append(["_ _"] * 20)
        else:
            A.append(["   "] * 20)

    for i in range(1, 15):
        A[i][0] = "\ "
        A[i][19] = " /"

    A[protagonist_y][protagonist_x] = ' ^ '

    A[0][0] = 'Score: ' + str(score)
    for i in range(15):
        print()
        for j in range(20):
            print(A[i][j], end="")
    print()


# Функции, отвечающие за действия ГГ. Принимает и обрабатывает нажатие клавиш.
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
    global score, act
    global projectile_y, projectile_x, protagonist_y, protagonist_x
    projectile_y = protagonist_y
    projectile_x = protagonist_x

    def anima():
        global projectile_y, projectile_x, score, act
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
            act = False

        time.sleep(0.001)

    while act:
        sheet(anima())


def shot():
    global animation, act
    animation = threading.Thread(target=projectile)
    animation.start()
    animation.join()
    act = True


if __name__ == "__main__":
    greetings()
    while True:
        keyboard.hook(action)
        keyboard.wait()
