import re

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

def is_game_possible(sets):
    for set in sets:
        for color in ["red", "green", "blue"]:
            if color in set:
                if total_cubes[color] < set[color]:
                    return False
    return True

with open("input.txt") as f:
    id_sum = 0
    for line in f:
        line = line.strip()
        print(line)
        game_id, sets = parse_game(line)
        if is_game_possible(sets):
            id_sum += game_id

    print(id_sum)

