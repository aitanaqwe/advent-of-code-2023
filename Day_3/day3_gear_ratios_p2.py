import math
import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_3\day3_puzzle_input.txt', 'r').read().splitlines()

def add_padding(puzzle_input, pad_char='.', pad_length=1):

    puzzle_input.insert(0, pad_char * len(puzzle_input[0]))
    for i in range(len(puzzle_input)):
        puzzle_input[i] = pad_char * pad_length + puzzle_input[i] + pad_char * pad_length
    puzzle_input.append(pad_char * len(puzzle_input[0]))

    return puzzle_input

add_padding(puzzle_input)

result = 0

split_input = []
for i, line in enumerate(puzzle_input):
    nums = re.finditer('(\d+)', line)
    split_input+= [list(line)]
    for num in nums:
        for j in range(num.start(),num.end()):
            split_input[i][j] = num.group()

for i, line in enumerate(puzzle_input):
    asts = re.finditer(r'\*', line)
    ast_indices = [ast.start() for ast in asts]

    for ast_indice in ast_indices:
        part_sum = 0
        part_list = []
        for string in split_input[i-1][ast_indice-1:ast_indice+2]:
            if string.isnumeric():
                if int(string) not in part_list:
                    part_list.append(int(string))
                    part_sum += 1
        for string in split_input[i][ast_indice-1:ast_indice+2]:
            if string.isnumeric():
                if int(string) not in part_list:
                    part_list.append(int(string))
                    part_sum += 1
        for string in split_input[i+1][ast_indice-1:ast_indice+2]:
            if string.isnumeric():
                if int(string) not in part_list:
                    part_list.append(int(string))
                    part_sum += 1
        if part_sum == 2:
            result += math.prod(part_list)

print(result)


        