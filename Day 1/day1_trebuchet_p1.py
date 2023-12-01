puzzle_input = open('day1_puzzle_input.txt', 'r').read().splitlines()

result = 0
for line in puzzle_input:
    first_dig = next((char for char in line if char.isdigit()))
    last_dig = next((char for char in line[::-1] if char.isdigit()))
    conc =  first_dig + last_dig
    result += int(conc)

print(result)