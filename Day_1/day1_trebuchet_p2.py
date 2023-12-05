puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_1\day1_puzzle_input.txt', 'r').read().splitlines()

also_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_first_and_last(line):
    first_value = 0
    first_index = len(line)
    last_value = 0
    last_index = 0

    for i in range(len(line)) :
        if line[i].isdigit():
            if i <= first_index:
                first_value = line[i]
                first_index = i
            if i >= last_index:
                last_value = line[i]
                last_index = i
              
    for digit in also_digits:
            if digit in line:
                i = line.find(digit)
                if i <= first_index:
                    first_value = also_digits.index(digit) + 1
                    first_index = i
                elif i >= last_index:
                    last_value = also_digits.index(digit) + 1
                    last_index = i
                    
    return first_value, last_value

result = 0

for line in puzzle_input:
    first_dig, last_dig = get_first_and_last(line)
    conc =  str(first_dig) + str(last_dig)
    result += int(conc)

print(result)