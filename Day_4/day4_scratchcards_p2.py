import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_4\day4_puzzle_input.txt', 'r').read().splitlines()

card_instances = [1] * len(puzzle_input)

for i, line in enumerate(puzzle_input):
    winners, numbers = [map(int, part.split()) for part in line.split(':')[1].split('|')]
    common_numbers = set(winners) & set(numbers)
    matches = len(common_numbers)

    for card in range(card_instances[i]):
        for j in range(matches):
            card_instances[i+j+1] += 1

result = sum(card_instances)
print (result)