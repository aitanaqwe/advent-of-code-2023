puzzle_input = open('C:\Repos\\advent-of-code-2023\Day_5\day5_test_puzzle_input.txt', 'r').read()

maps = {}
current_map_name = ""

for line in puzzle_input.splitlines():
    if line.startswith("seeds:"):
        current_map_name = "seeds"
        maps[current_map_name] = list(map(int, line.split(":")[1].split()))
    elif line.endswith(":"):
        current_map_name = line[:-1].replace(" ", "_").replace("-", "_")
        maps[current_map_name] = []
    elif line:
        values = list(map(int, line.split()))
        maps[current_map_name].append(values)

for seed in maps['seeds']:
    soil = 0
    for line in maps['seed_to_soil_map']:
        if seed in range(line[1], line[1] + line[2]):
            soil = line[0] + (seed - line[1])
    if soil == 0:
        soil = seed

    print (soil)

print(maps)
