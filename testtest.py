import os, time, keyboard, threading
A =[]
protagonist_y = 13
protagonist_x = 9
score = 0


def sheet(function):
    global protagonist_y, protagonist_x, score
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

    A[protagonist_y][protagonist_x]= ' ^ '
    A[0][0] = 'Score: ' + str(score)
    for i in range(15):
        print()
        for j in range(20):
            print(A[i][j], end="")
    print()


def shot():
    def kill(y, x):
        global score
        A[y][x] = " * "
        score += 100
        time.sleep(0.5)
        return ' * '

    global score
    projectile_y = protagonist_y
    projectile_x = protagonist_x
    # for i in range(1, 12):
    if A[projectile_y][projectile_x] == " | ":
        A[projectile_y][projectile_x] = "   "
    elif A[projectile_y][projectile_x] == "_|_":
        A[projectile_y][projectile_x] = "_ _"

    if A[projectile_y - 1][projectile_x] == "   ":
        projectile_y -= 1
        A[projectile_y][projectile_x] = " | "

    elif A[projectile_y - 1][projectile_x] == "_ _":
        projectile_y -= 1
        A[projectile_y][projectile_x] = "_|_"

    else:
        projectile_y -= 1
        A[projectile_y][projectile_x] = kill(projectile_y, projectile_x)

        time.sleep(0.5)


shooting = threading.Thread(target=sheet(shot))
shooting.start()