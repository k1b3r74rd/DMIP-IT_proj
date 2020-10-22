import keyboard, os, time

A = []

# Начальные координаты протагониста + счёт
protagonist_y = 13
protagonist_x = 9
score = 0

# Тестовые переменные под снаряд
projectile_y = 12
projectile_x = 9
projectile_type = " | "


# Стартовое окно
def greetings():
    def start(enter):
        if enter.name == "enter":
            sheet(projectile_y, projectile_x, projectile_type)

    os.system('cls')
    print('Welcome to da game. Press "Enter" to start da game.')
    keyboard.hook(start)


# Рисует  и обновляет поле. Основая, по сути, функция
# При тесте протагониста, заменить переменные снаряда на переменные протагониста (протагонист_у, протагонист_х)
def sheet(projectile_y, projectile_x, projectile_type):
    # def protagonist(protagonist_y, protagonist_x):
    #     A[protagonist_y][protagonist_x] = " ^ "

    def projectile(projectile_y, projectile_x, projectile_type):
        A[projectile_y][projectile_x] = projectile_type

    os.system('cls')
    for i in range(1, 15):
        if i == 8:
            A.append(["_ _"] * 20)
        else:
            A.append(["   "] * 20)

        A[i][0] = "\ "
        A[i][19] = " /"

    # protagonist(protagonist_y, protagonist_x)
    projectile(projectile_y, projectile_x, projectile_type)
    A[0][0] = 'Score: ' + str(score)
    for i in range(15):
        print()
        for j in range(20):
            print(A[i][j], end="")
    print()


def protagonist_movement(button):
    # global protagonist_x
    #
    # if button.name == "left" and button.event_type == "down":
    #     if protagonist_x - 1 == 0:
    #         pass
    #     else:
    #         A[protagonist_y][protagonist_x] = "   "
    #         protagonist_x -= 1
    #         sheet(protagonist_y=protagonist_y, protagonist_x=protagonist_x)
    #
    # elif button.name == "right" and button.event_type == "down":
    #     if protagonist_x + 1 == 19:
    #         pass
    #     else:
    #         A[protagonist_y][protagonist_x] = "   "
    #         protagonist_x += 1
    #         sheet(protagonist_y=protagonist_y, protagonist_x=protagonist_x)

    if button.name == "space" and button.event_type == "down":
        shot()


# Выстрел снаряда, анимация и обработка полета
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
    for i in range(1, 12):
        if A[projectile_y][projectile_x] == " | ":
            A[projectile_y][projectile_x] = "   "
        elif A[projectile_y][projectile_x] == "_|_":
            A[projectile_y][projectile_x] = "_ _"

        if A[projectile_y - 1][projectile_x] == "   ":
            projectile_y -= 1
            projectile_type = " | "

        elif A[projectile_y - 1][projectile_x] == "_ _":
            projectile_y -= 1
            projectile_type = "_|_"

        else:
            projectile_y -= 1
            projectile_type = kill(projectile_y, projectile_x)

        sheet(projectile_y=projectile_y, projectile_x=projectile_x, projectile_type=projectile_type)

        time.sleep(0.005)


if __name__ == "__main__":
    greetings()
    while True:
        keyboard.hook(protagonist_movement)
        keyboard.wait()
