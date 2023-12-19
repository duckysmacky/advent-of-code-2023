colors = ["red", "green", "blue"]
avaliable = {"red": 12, "green": 13, "blue": 14}
counter = 0

with open("./Day2/input.txt") as f:
    games = f.readlines()
    
for i in range(len(games)):
    games[i] = games[i].removeprefix(f"Game {i + 1}: ")
    games[i] = games[i].split("; ")

for index, sets in enumerate(games):
    print(f"\n\nGame {index + 1}: {sets}")
    avaliableSets = 0
    for i in range(len(sets)):
        set = sets[i].split(", ")
        cubes = {}
        for set_cubes in set:
            for color in colors:
                if color in set_cubes:
                    cubes[color] = set_cubes.strip().removesuffix(f" {color}")
        print(f"\nCubes per set: {cubes}")
        avaliableColors = 0
        for color in colors:
            if color in cubes:
                print(f"{color.upper()}: Avaliable {avaliable[color]} | Cubes {cubes[color]}")
                if int(cubes[color]) <= avaliable[color]:
                    avaliableColors += 1
                    print(f"Color {color} is avaliable")
        if avaliableColors == len(cubes.keys()):
            avaliableSets += 1
    if avaliableSets == len(sets):
        counter += (index + 1);
        print(f"Game {index + 1} is valid")
                
print(counter)