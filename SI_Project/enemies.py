# Модуль, отвечащий за "спавн" и движение противников.

import keyboard, os, time, threading
# from SI_Project.sheet import sheet, first_sheet
# import SI_Project.action

A = []
B = []

protagonist_y = 13
protagonist_x = 9
score = 0

game = True


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
                time.sleep(0.5)
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


def end():
        os.system('cls')
        print('SCORE // SCORE // SCORE // SCORE // SCORE // SCORE // ')
        time.sleep(30)


if __name__ == "__main__":
    enemy_generate()
    first_sheet()

    enemy()

    end()
