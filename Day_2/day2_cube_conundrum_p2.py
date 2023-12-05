import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_2\day2_puzzle_input.txt', 'r').read().splitlines()

games_power_sum = 0 

def get_games_power(game_match, cube_matches):
    MAX_VALUES = {'red': 0, 'green': 0, 'blue': 0}
    for combo in cube_matches:
        color, value = combo[1], int(combo[0])
        MAX_VALUES[color] = max(MAX_VALUES[color], value)

    game_power = MAX_VALUES['red'] * MAX_VALUES['green'] * MAX_VALUES['blue']
    return int(game_power)


for line in puzzle_input:
    game_match = re.findall('Game (\d+)', line)
    cube_matches = re.findall('(\d+) (\w+)', line)
    games_power_sum += get_games_power(game_match, cube_matches)

print (games_power_sum)