# Первый файл для тестов и испытаний ( функции и механики, относящиеся к проекту).

import keyboard, os, time, threading
# from SI_Project.sheet import sheet, first_sheet
# import SI_Project.action

A = []
B = []
act = True
game = True

protagonist_y = 13
protagonist_x = 9
score = 0


# Стартовое окно.
def greetings():
    def start(enter):
        enemy_generate()
        if enter.name == "enter":
            potok.start()
            first_sheet()
            enemy()
            potok.join()

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


# Функции, отвечающие за "спавн" и движение противников.
def spawn():
    global A, B, enemy_y, game, end

    def enemy_first_spawn(enemy_y):
        for x in range(1, 20):
            A[enemy_y][x] = B[enemy_y][x]

    def enemy_move(enemy_y):
        for x in range(1, 20):
            A[enemy_y][x] = A[enemy_y - 1][x]
            A[enemy_y - 1][x] = A[enemy_y - 2][x]
            A[enemy_y - 2][x] = A[enemy_y - 3][x]
            A[enemy_y - 3][x] = '   '

    while game:
        for enemy_y in range(1, 10):
            if enemy_y < 4:
                sheet(enemy_first_spawn(enemy_y))
                time.sleep(0.3)
            else:
                time.sleep(5)
                sheet(enemy_move(enemy_y))

        for i in range(20):
            if A[9][i] != '_ _':
                print('GAME OVER, YOU LOSE // GAME OVER, YOU LOSE // GAME OVER')
                time.sleep(2)
                game = False
                break

            elif A[9][i] == '_ _':
                print('YOU WIN // YOU WIN // YOU WIN // YOU WIN // YOU WIN // ')
                time.sleep(2)
                game = False
                break


def enemy():
    global enemy_anima

    enemy_anima = threading.Thread(target=spawn)
    enemy_anima.start()
    enemy_anima.join()


# Финальный экран со счетом.
def end():
    os.system('cls')
    print('SCORE // SCORE // SCORE // SCORE // SCORE // SCORE // ')
    time.sleep(30)


potok = threading.Thread(keyboard.hook(action))


if __name__ == "__main__":
    greetings()
    # while True:
    #     keyboard.hook(action)
    #     keyboard.wait()
