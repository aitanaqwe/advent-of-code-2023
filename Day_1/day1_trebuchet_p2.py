import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_1\day1_puzzle_input.txt', 'r').read().splitlines()

also_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

result = 0
for line in puzzle_input:
    for digit in also_digits:
        if digit in line:
            print(digit)

    first_dig = next((char for char in line if char.isdigit()))
    last_dig = next((char for char in line[::-1] if char.isdigit()))
    conc =  first_dig + last_dig
    result += int(conc)
print(result)