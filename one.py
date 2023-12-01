import re

def extract(y):
    lines = y.split('\n')
    sum = 0

    for line in lines:
        nums = re.findall(r'\d+', line)
        if nums:
            x = int(nums[0][0] + nums[-1][-1])
            sum += x

    return sum

with open('input.txt', 'r') as file:
    puzzle_input = file.read()
res = extract(puzzle_input)
print(res)
