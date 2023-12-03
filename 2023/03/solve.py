import re
import operator as op
import itertools

def find_symbol_locations(content : list, regex):
    """
    List is sorted by ascending y because that's the order in which the entries are discovered.
    """
    foo = re.compile(regex)
    # [(x, y), ...]
    locations = []
    y = 0;
    for line in content:
        matches = foo.finditer(line)
        for match in matches:
            locations.append((match.start(), y))
        y += 1
    return locations

def generate_possible_number_locations(symbol_locations):
    possible_locations = []
    for location in symbol_locations:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                possible_locations.append((location[0] + dx, location[1] + dy))
    return possible_locations

def find_adjacent_numbers_ids(content, possible_number_locations):
    """
    Returns a set of adjacent numbers ids for the given possible number locations.
    [{0, 78, 3}, {2}, ...]
    """
    numbers = set()
    for possible_location in possible_number_locations:
        if content[possible_location[1]][possible_location[0]] >= 0:
            numbers.add(content[possible_location[1]][possible_location[0]])
    return numbers

def generate_number_map(content : list):
    """
    Returns {0 : 468, 1: 984}, [[...000...*...], [111...22222], ...]
    """
    content_with_number_indices = []
    number_map = {}
    number_regex = re.compile("\d+")
    number_idx = 0
    for line in content:
        processed_line = [-1] * len(line)
        for match in number_regex.finditer(line):
            number_map[number_idx] = int(line[match.start():match.end()])
            for i in range(match.start(), match.end()):
                processed_line[i] = number_idx
            number_idx += 1
        content_with_number_indices.append(processed_line)
    return number_map, content_with_number_indices            
        
def parse_number(text, x):
    """
    x points to one of the number's digits.
    """
    start_idx = x
    while 0 <= start_idx and text[start_idx - 1].isdigit():
        start_idx -= 1
    end_idx = x
    # No + 1 because we need the index after the last digit
    while end_idx < len(text) and text[end_idx].isdigit():
        end_idx += 1
    return int(text[start_idx:end_idx]), start_idx, end_idx

def find_gear_ratios_ids(content_with_ids, gearbox_locations):
    """
    Returns [(id, id), ...]
    """
    gear_ratios = []
    for gearbox in gearbox_locations:
        adjacent_numbers = set()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                x = gearbox[0] + dx
                y = gearbox[1] + dy
                i = content_with_ids[y][x] 
                if i >= 0:
                    adjacent_numbers.add(i)
        if len(adjacent_numbers) == 2:
            gear_ratios.append(adjacent_numbers)
    return gear_ratios

with open("input.txt") as f:
    content = [line.strip() for line in f]
    number_map, content_with_ids = generate_number_map(content)
    all_symbols_regex = "[^\.\d]"
    locations = find_symbol_locations(content, all_symbols_regex)
    possible_number_locations = generate_possible_number_locations(locations)
    number_ids = find_adjacent_numbers_ids(content_with_ids, possible_number_locations)
    foo = 0
    for number_id in number_ids:
        foo += number_map[number_id]
    print("Part 1:", foo)

    gearbox_locations = find_symbol_locations(content, "\*")
    gear_ratios = find_gear_ratios_ids(content_with_ids, gearbox_locations)
    gear_ratios = map(lambda t: map(lambda idx: number_map[idx], t), gear_ratios)
    
    print("Part 2:", sum(itertools.starmap(op.mul, gear_ratios)))
