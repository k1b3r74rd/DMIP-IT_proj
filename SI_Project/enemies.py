# Модуль, отвечащий за "спавн" и движение противников.

import keyboard, os, time, threading
# from SI_Project.sheet import sheet, first_sheet
# import SI_Project.action

A = []
enemy_y = 1
enemy_x = 1

protagonist_y = 13
protagonist_x = 9
score = 0

game = True
end = True


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


def spawn():
    global enemy_x, enemy_y
    time.sleep(0.001)
    A[enemy_y][enemy_x] = ')-('
    if enemy_x != 19:
        enemy_x += 1
    else:
        enemy_x -= 18
        enemy_y += 1

    if enemy_y == 9:
        print('game_over')
        enemy_anima.join()


def enemy():
    global enemy_anima
    enemy_anima = threading.Thread(target=spawn())
    enemy_anima.start()


# if __name__ == "__main__":
#     first_sheet()
#     while game:
#         sheet(enemy())
#
#     while end:
#         os.system('cls')
#         print('YOU LOSE')
#         time.sleep(10000)