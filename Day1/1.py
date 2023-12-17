with open("./Day1/input.txt") as f:
    lines = f.readlines()

number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

nums = []
for index, line in enumerate(lines):
    line_nums = []
    for i in range(len(line)):
        print(f"\nCurrent Line: {line}\nCurrent index: {line[i]}")
        
        if line[i].isnumeric():
            line_nums.append(int(line[i]))
        
        for word_index, word in enumerate(number_words):
            if word in line[i:len(word)]:
                line_nums.append(word_index + 1)
                print(f"Word: {word}\nNumber: {word_index + 1}")
        
    print(line_nums)
    print("\n")   
    nums.append(line_nums[0] + line_nums[-1])

    
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
print(sum(nums))