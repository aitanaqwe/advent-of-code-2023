import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_3\day3_test_puzzle_input.txt', 'r').read().splitlines()

for i, line in enumerate(puzzle_input):
    nums = re.finditer('(\d+)', line)
    num_indices = [(num.group(), num.start(), num.end() - 1) for num in nums]
    print(num_indices)
    