with open("./Day3/input.txt") as f:
    lines = f.readlines()

sum = 0

input = []
for y in range(len(lines)):
    line = []
    for x in range(len(lines[y])):
        line.append(lines[y][x])
    input.append(line)

input = input[0:2]
for l in input:
    print(l)

def search_symbols(input, y, x):
    for offset_y in range(-1, 2):
        for offset_x in range(-1, 2):
            if y + offset_y >= 0 and y + offset_y < len(input):
                if x + offset_x >= 0 and x + offset_x < len(input[0]):
                    check_pos = input[y + offset_y][x + offset_x]
                    if not(check_pos.isnumeric()) and check_pos != "." and check_pos != "\n":
                        print(f"Symbol {check_pos} found at {y + offset_y};{x + offset_x}")
                        return True
    return False

for y, line in enumerate(input):
    number_ = []
    valid_numbers = 0
    for x, symbol in enumerate(input[y]):
        number = ""
        if symbol.isnumeric():
            number_.append(symbol)
            for num in number_: number += num
            number = int(number)
            
            print(f"Given {symbol} at {y};{x}")
            print(f"[D] Valid numbers {valid_numbers}, %10 {valid_numbers % 10}, Input-1 {input[y][x-1]}")
            if search_symbols(input, y, x):
                print(f"Symbol {symbol} is valid")
                valid_numbers = number
            elif input[y][x-1].isnumeric() and x != 0:
                if valid_numbers % 10 == int(input[y][x-1]):
                    valid_numbers = number
        elif symbol == ".":
            sum += valid_numbers
            if valid_numbers != 0:
                print(f"\n{valid_numbers} is valid! Sum: {sum}\n")
            valid_numbers = 0
            number_ = []
            
print(f"Answer: {sum}")