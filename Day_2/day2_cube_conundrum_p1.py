import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_2\day2_test_puzzle_input.txt', 'r').read().splitlines()

pattern = re.compile('Game (\d+): (\d+) (\w+)')

for line in puzzle_input:
    matches = pattern.findall(line)

print (matches)