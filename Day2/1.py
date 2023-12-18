colors = ["red", "green", "blue"]

with open("./Day2/test.txt") as f:
    games = f.readlines()
    
for i in range(len(games)):
    games[i] = games[i].removeprefix(f"Game {i + 1}: ")
    games[i] = games[i].split("; ")

counter = 0
for index, sets in enumerate(games):
    print(f"\nSet: {sets}")
    for i in range(len(sets)):
        set = sets[i].split(", ")
        cubes = {}
        for set_cubes in set:
            for color in colors:
                if color in set_cubes:
                    cubes[color] = set_cubes.strip().removesuffix(f" {color}")
        print(f"Cubes per set: {cubes}")