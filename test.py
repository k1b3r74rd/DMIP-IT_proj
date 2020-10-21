import keyboard, os
A = []
protagonist_y = 13
protagonist_x = 9


def protagonist(y, x):
    A[y][x] = " ^ "


def sheet(y, x):
    os.system('cls')
    for i in range(15):
        if i in range(0, 8):
            A.append([" * "] * 20)
        elif i == 8:
            A.append(["_ _"] * 20)
        elif i in range(9, 15):
            A.append(["   "] * 20)

        A[i][0]="\ "
        A[i][19] = " /"

    protagonist(y, x)

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


def print_pressed_keys(button):
    print(button.event_type,"\n", button.name)


sheet(protagonist_y, protagonist_x)
keyboard.hook(protagonist_move)
keyboard.wait()
