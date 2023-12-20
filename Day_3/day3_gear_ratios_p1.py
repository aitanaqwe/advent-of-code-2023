import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_3\day3_test_puzzle_input.txt', 'r').read().splitlines()

def add_padding(puzzle_input, pad_char='.', pad_length=1):

    puzzle_input.insert(0, pad_char * len(puzzle_input[0]))
    for i in range(len(puzzle_input)):
        puzzle_input[i] = pad_char * pad_length + puzzle_input[i] + pad_char * pad_length
    puzzle_input.append(pad_char * len(puzzle_input[0]))

    return puzzle_input

add_padding(puzzle_input)

result = 0

for i, line in enumerate(puzzle_input):
    nums = re.finditer('(\d+)', line)
    num_indices = [(num.group(), num.start(), num.end() - 1) for num in nums]
    print(num_indices)

    for num in num_indices:

        value = int(num[0])
        first_index = num[1]
        last_index = num[2]

        
        for char in puzzle_input[i-1][first_index-1:last_index+2]:
            if char.isascii() and not char.isalnum() and not char == '.':
                print(value)
                result += value
        for char in puzzle_input[i][first_index-1:last_index+2]:
            if char.isascii() and not char.isalnum() and not char == '.':
                print(value)
                result += value
        for char in puzzle_input[i+1][first_index-1:last_index+2]:
            if char.isascii() and not char.isalnum() and not char == '.':
                print(value)
                result += value
        
print(result)

        