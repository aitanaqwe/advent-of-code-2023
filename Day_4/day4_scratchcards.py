import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_4\day4_puzzle_input.txt', 'r').read().splitlines()

result = 0

for line in puzzle_input:
    potencia = 0
    card_worth = 0

    winners = [int(num) for num in line.split(':')[1].split('|')[0].split()]
    numbers = [int(num) for num in line.split(':')[1].split('|')[1].split()]

    for winner in winners:
        if winner in numbers:
            potencia += 1
    
    if potencia != 0:
        card_worth = 2**(potencia-1)
    result += card_worth

print (result)