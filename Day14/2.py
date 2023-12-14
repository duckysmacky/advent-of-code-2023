with open("./Day14/input.txt", "r") as f:
    fc = [x.strip() for x in f.readlines()]
    game = [[x[col] for x in fc] for col in range(len(fc[0]))]

NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3


def roll(dir, col):
    if dir == NORTH or dir == WEST:
        for symb in range(1, len(game[col])):
            if game[col][symb] == "O":
                new_ind = symb
                for i in range(len(game[col][:symb]))[::-1]:
                    if game[col][i] != ".": break
                    if game[col][i] == ".":
                        if(i >= 1 and game[col][i - 1] != ".") or i == 0:
                            new_ind = i
                            break
                game[col][symb], game[col][new_ind] = game[col][new_ind], game[col][symb]
    elif dir == SOUTH or dir == EAST:
        for symb in range(len(game[col]))[::-1]:
            if game[col][symb] == "O":
                new_ind = symb
                for i in range(len(game[col][symb + 1:])):
                    if game[col][i + symb + 1] != ".": break
                    if game[col][i + symb + 1] == ".":
                        if (i + symb + 2 < len(game[col]) and game[col][i + symb + 2] != ".") or i + symb + 2 == len(game[col]):
                            new_ind = i + symb + 1
                            break
                game[col][symb], game[col][new_ind] = game[col][new_ind], game[col][symb]

s = 0
for i in range(1000000000):
    print("on iteration", i)
    for col in range(len(game)): roll(NORTH, col)

    game = [[x[c] for x in game] for c in range(len(game[0]))]
    for col in range(len(game)): roll(WEST, col)

    game = [[x[c] for x in game] for c in range(len(game[0]))][::-1]
    for col in range(len(game)): roll(SOUTH, col)

    game = [[x[c] for x in game][::-1] for c in range(len(game[0]))]
    for col in range(len(game)): roll(EAST, col)

    game = [[x[c] for x in game] for c in range(len(game[0]))][::-1]
for col in range(len(game)):
    for symb in range(len(game[col])):
        if game[col][symb] == "O":
            s += len(game[col]) - symb

print(s)