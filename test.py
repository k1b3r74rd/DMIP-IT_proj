# Первый файл для тестов и испытаний ( функции и механики, относящиеся к проекту).

import keyboard, os, time, threading

A = []
B = []
act = True
game = True

protagonist_y = 13
protagonist_x = 9
score = 0


# Стартовое окно.
def start_window():
    global potok, enemy_anima

    def start(enter):
        global potok, enemy_anima
        enemy_generate()
        if enter.name == "enter" and enter.event_type == "down":
            keyboard.block_key("enter")
            first_sheet()
            potok.start()
            enemy_anima.start()

    os.system('cls')
    print('Made by Zolotarev Maxim. Tomsk. 2020. ', end='\n\n\n\n\n')
    print('Welcome to "Space Invaders" clone game. Press "Enter" to start.', end='\n\n\n\n\n')
    print('Controls:\n Space - shoot \n right arrow - move right \n left arrow - move left')
    keyboard.hook(start)
    keyboard.wait()


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
            a = threading.Thread(sheet(move_left()))
            a.start()
            a.join()

    elif button.name == "right" and button.event_type == "down":
        if protagonist_x + 1 == 19:
            pass
        else:
            a = threading.Thread(sheet(move_right()))
            a.start()
            a.join()

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
        elif A[projectile_y][projectile_x] == " * ":
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


# Функция, отвечающая за создание противников.
def enemy_generate():
    global B
    for y in range(4):
        B.append([r'\|/'] * 20)
        for x in range(20):
            if y % 2 != 0:
                if x % 2 != 0:
                    B[y][x] = '   '

            elif y % 2 != 1:
                if x % 2 != 1:
                    B[y][x] = '   '


# Функции, отвечающие за "спавн" и движение противников, строка за строкой. Также отвечают за конец игры.
def spawn():
    global A, B, enemy_y, game, end, potok, enemy_anima

    def enemy_first_spawn(enemy_y):
        for x in range(1, 19):
            print(A[enemy_y][x], ' ', B[enemy_y][x])
            A[enemy_y][x] = B[enemy_y - 1][x]
            print(A[enemy_y][x], ' ', B[enemy_y][x])

    def enemy_move(enemy_y):
        global game, potok, enemy_anima
        for x in range(1, 20):
            if A[enemy_y][x] == '_ _' and A[enemy_y - 1][x] == '   ':
                pass
            elif A[enemy_y][x] == '_ _':
                A[enemy_y][x] = A[enemy_y - 1][x]
                print('GAME OVER // GAME OVER // GAME OVER // GAME OVER // GAME OVER')
                potok.join()
                enemy_anima.join()
                game = False
                time.sleep(0.5)
                end()
                break
            else:
                A[enemy_y][x] = A[enemy_y - 1][x]

            if A[enemy_y - 1][x] == '_ _' and A[enemy_y - 2][x] == '   ':
                pass
            elif A[enemy_y - 1][x] == '_ _':
                A[enemy_y - 1][x] = A[enemy_y - 2][x]
                print('GAME OVER // GAME OVER // GAME OVER // GAME OVER // GAME OVER')
                potok.join()
                enemy_anima.join()
                game = False
                time.sleep(0.5)
                end()
                break
            else:
                A[enemy_y - 1][x] = A[enemy_y - 2][x]

            if A[enemy_y - 2][x] == '_ _' and A[enemy_y - 3][x] == '   ':
                pass
            elif A[enemy_y - 2][x] == '_ _':
                A[enemy_y - 2][x] = A[enemy_y - 3][x]
                print('GAME OVER // GAME OVER // GAME OVER // GAME OVER // GAME OVER')
                potok.join()
                enemy_anima.join()
                game = False
                time.sleep(0.5)
                end()
                break
            else:
                A[enemy_y - 2][x] = A[enemy_y - 3][x]

            A[enemy_y - 3][x] = '   '

    while game:
        for enemy_y in range(1, 12):
            if enemy_y < 4:
                sheet(enemy_first_spawn(enemy_y))
                time.sleep(0.3)
            else:
                time.sleep(0.5)
                sheet(enemy_move(enemy_y))

    potok.join()
    enemy_anima.join()
    game = False
    time.sleep(0.5)
    end()


# Финальный экран со счетом.
def end():
    global potok, enemy_anima
    potok.join()
    enemy_anima.join()
    os.system('cls')
    print('SCORE // SCORE // SCORE // SCORE // SCORE // SCORE // ')
    time.sleep(30)


def keyb_act():
    while True:
        keyboard.hook(action)
        keyboard.wait()


enemy_anima = threading.Thread(target=spawn)
potok = threading.Thread(target=keyb_act)

if __name__ == "__main__":
    start_window()
    end()
