import keyboard, os
A = []
protagonist_y = 13
protagonist_x = 9
score = 0


def greetings():
    def start(enter):
        if enter.name == "enter":
            sheet(protagonist_y, protagonist_x)
    os.system('cls')
    print('Welcome to da game. Press "Enter" to start da game.')
    keyboard.hook(start)


def sheet(y, x):
    def protagonist(y, x):
        A[y][x] = " ^ "

    os.system('cls')
    for i in range(1, 15):
        if i == 8:
            A.append(["_ _"] * 20)
        else:
            A.append(["   "] * 20)

        A[i][0]="\ "
        A[i][19] = " /"

    protagonist(y, x)
    A[0][0] = 'Score: ' + str(score)
    for i in range(15):
        print()
        for j in range(20):
            print(A[i][j], end="")


def protagonist_move(button):
    global protagonist_x

    if button.name == "left" and button.event_type == "down":
        if protagonist_x - 1 == 0:
            pass
        else:
            A[protagonist_y][protagonist_x] = "   "
            protagonist_x -= 1
            sheet(protagonist_y, protagonist_x)

    elif button.name == "right" and button.event_type == "down":
        if protagonist_x + 1 == 19:
            pass
        else:
            A[protagonist_y][protagonist_x] = "   "
            protagonist_x += 1
            sheet(protagonist_y, protagonist_x)


if __name__ == "__main__":
    greetings()
    while True:
        keyboard.hook(protagonist_move)
        keyboard.wait()

