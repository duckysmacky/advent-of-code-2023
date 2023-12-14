counter = 0

with open("./Day12/input.txt", "r") as f:
    lines = f.readlines()

locs = lines.copy()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    locs[i] = lines[i][lines[i].find(" ") + 1:].split(",")
    for n in range(len(locs[i])):
        locs[i][n] = int(locs[i][n])
    lines[i] = lines[i][:lines[i].find(" ")]
    print(lines[i], locs[i])
    
    for l in lines[i]:
        if l == '?':
            
        