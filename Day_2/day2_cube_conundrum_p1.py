import re

puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_2\day2_puzzle_input.txt', 'r').read().splitlines()

max_red = 12
max_green = 13
max_blue = 14

game_pattern = re.compile('Game (\d+)')
cubes_pattern = re.compile('(\d+) (\w+)')

possible_games_sum = 0 

def get_possible_games(game_match, cube_matches):
    is_possible = True
    for combo in cube_matches:
        if combo[1] == 'red':
            if int(combo[0]) > max_red:
                is_possible = False
        elif combo[1] == 'green':
            if int(combo[0]) > max_green:
                is_possible = False
        elif combo[1] == 'blue':
            if int(combo[0]) > max_blue:
                is_possible = False

    if is_possible == True:
        return int(game_match[0])
    else:
        return 0


for line in puzzle_input:
    game_match = re.findall('Game (\d+)', line)
    cube_matches = re.findall('(\d+) (\w+)', line)
    possible_games_sum += get_possible_games(game_match, cube_matches)

print (possible_games_sum)