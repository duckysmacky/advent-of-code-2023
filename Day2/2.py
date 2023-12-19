colors = ["red", "green", "blue"]
minColors = {}
sumOfPower = 0

with open("./Day2/test.txt") as f:
    games = f.readlines()
    
for i in range(len(games)):
    games[i] = games[i].removeprefix(f"Game {i + 1}: ")
    games[i] = games[i].split("; ")

for index, sets in enumerate(games):
    print(f"\n\nGame {index + 1}: {sets}")
    minColorsInGame = {"red": 0, "green": 0, "blue": 0}
    for i in range(len(sets)):
        set = sets[i].split(", ")
        cubes = {}
        for set_cubes in set:
            for color in colors:
                if color in set_cubes:
                    cubes[color] = set_cubes.strip().removesuffix(f" {color}")
        print(f"\nCubes per set: {cubes}")
        
        minColorsInSet = {"red": 0, "green": 0, "blue": 0}
        for color in colors:
            if color in cubes:
                minColorsInSet[color] = max(minColorsInSet[color], int(cubes[color]))
        print(minColorsInSet)   
        for color in colors:
            if color in cubes:
                minColorsInGame[color] = max(minColorsInGame[color], minColorsInSet[color])
        print(minColorsInGame)
    multValue = 0
    for value in minColorsInGame.values():
        multValue *= value
    sumOfPower += multValue
    
print(sumOfPower)