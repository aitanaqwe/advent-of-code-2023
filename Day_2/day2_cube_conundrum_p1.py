import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_2\day2_puzzle_input.txt', 'r').read().splitlines()

MAX_VALUES = {'red': 12, 'green': 13, 'blue': 14}

possible_games_sum = 0 

def get_possible_games(game_match, cube_matches):
    for combo in cube_matches:
        color, value = combo[1], int(combo[0])
        if value > MAX_VALUES.get(color):
            return 0
    return int(game_match[0])


for line in puzzle_input:
    game_match = re.findall('Game (\d+)', line)
    cube_matches = re.findall('(\d+) (\w+)', line)
    possible_games_sum += get_possible_games(game_match, cube_matches)

print (possible_games_sum)