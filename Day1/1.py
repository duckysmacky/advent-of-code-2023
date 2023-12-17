with open("./Day1/input.txt") as f:
    lines = f.readlines()

nums = []
for index, line in enumerate(lines):
    line_nums = []
    for i in range(len(line)):
        if line[i].isnumeric():
            line_nums.append(line[i])
    nums.append(line_nums[0] + line_nums[-1])
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(sum(nums))