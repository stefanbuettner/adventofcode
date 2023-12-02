import re
import itertools as it
import operator as op

total_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse_game(line):
    game, sets_combined = line.split(": ")
    _, game_id = game.split(" ")
    game_id = int(game_id)
    sets = sets_combined.split("; ")
    parsed_sets = []
    for set in sets:
        cubes = set.split(", ")
        cube_results = {}
        for cube in cubes:
            cube_count, color = cube.split(" ")
            cube_results[color] = int(cube_count)
        parsed_sets.append(cube_results)
    return game_id, parsed_sets

colors = ["red", "green", "blue"]
def min_cubes_needed(sets):
    min_cubes = {color : 0 for color in colors}

    for set in sets:
        for color in colors:
            if color in set:
                min_cubes[color] = max(min_cubes[color], set[color])
    return min_cubes

#with open("example.txt") as f:
with open("input.txt") as f:
    power_sum = 0
    for line in f:
        line = line.strip()
        print(line)
        game_id, sets = parse_game(line)
        min_cubes = min_cubes_needed(sets)
        set_power = list(it.accumulate(min_cubes.values(), op.mul))[-1]
        power_sum += set_power

    print(power_sum)

