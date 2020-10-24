import keyboard, os, time, threading
# from SI_Project.sheet import sheet, first_sheet
# import SI_Project.action

A = []

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

    function()

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


def action(button):
    global protagonist_x
    global protagonist_y
    if button.name == "left" and button.event_type == "down":
        if protagonist_x - 1 == 0:
            pass
        else:
            move_left(protagonist_y, protagonist_x)

    elif button.name == "right" and button.event_type == "down":
        if protagonist_x + 1 == 19:
            pass
        else:
            move_right(protagonist_y, protagonist_x)

    elif button.name == "space" and button.event_type == "down":
        action.shot()


@sheet
def move_left(protagonist_y, protagonist_x):
    A[protagonist_y][protagonist_x] = "   "
    protagonist_x -= 1
    A[protagonist_y][protagonist_x] = ' ^ '


@sheet
def move_right(protagonist_y, protagonist_x):
    A[protagonist_y][protagonist_x] = "   "
    protagonist_x += 1
    A[protagonist_y][protagonist_x] = ' ^ '


if __name__ == "__main__":
    greetings()
    first_sheet()
    while True:
        keyboard.hook(action)
        keyboard.wait()
