import keyboard, random
A = []


def greetings():
    print('To start game, press Enter...')
    input()
    sheet()


def sheet():
    for i in range(15):
        if i == 13:
            A.append(["__"] * 20)
        elif i == 14:
            A.append(["  "] * 20)
            A[i][random.randint(1, 19)] = "^ "
        else:
            A.append(["* "] * 20)
        A[i][0]="\  "
        A[i][19] = " /"

    for i in range(15):
        print()
        # A[i][random.randint(1, 29)] = " * "
        for j in range(20):
            print(A[i][j], end="")


if __name__ == "__main__":
    greetings()
    input()
