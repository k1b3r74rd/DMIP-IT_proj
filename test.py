import keyboard, random
A = []


def sheet():
    global protagonist_y
    global protagonist_x
    for i in range(15):
        if i == 8:
            A.append(["_ _"] * 20)
        elif i in [9, 10, 11, 12, 14]:
            A.append(["   "] * 20)
        elif i == 13:
            A.append(["   "] * 20)
            protagonist_y = i
            protagonist_x = 9
            A[protagonist_y][protagonist_x] = " ^ "
        else:
            A.append([" * "] * 20)
        A[i][0]="\  "
        A[i][19] = " /"

    for i in range(15):
        print()
        for j in range(20):
            print(A[i][j], end="")


def protagonist_move(button):
    if button.name == "left":
        pass


def print_pressed_keys(button):
    print(button.event_type,"\n", button.name)


sheet()
# keyboard.hook(print_pressed_keys)
# keyboard.wait()