maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def print_maps():
    print(maps[0], end="")
    print(maps[1], end="")
    print(maps[2])
    print(maps[3], end="")
    print(maps[4], end="")
    print(maps[5])
    print(maps[6], end="")
    print(maps[7], end="")
    print(maps[8])


def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol



def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "x" and maps[i[1]] == "x" and maps[i[2]] == "x":
            win = "x"
        if maps[i[0]] == "0" and maps[i[1]] == "0" and maps[i[2]] == "0":
            win = "0"

    return win


game_over = False
player1 = True

while game_over == False:

    print_maps()

    if player1 == True:
        symbol = "x"
        step = int(input("Человек 1,ваш ход:"))
    else:
        symbol = "0"
        step = int(input("Человек 2, ваш ход:"))

    step_maps(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

print_maps()
print("Победил", win)
