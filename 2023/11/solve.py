import itertools as it
import bisect

example = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def find_galaxy_locations(content):
    locations = []
    for y in range(len(content)):
        for x in range(len(content[y])):
            if content[y][x] == "#":
                locations.append((x, y))
    return locations

def print_content(content):
    for line in content:
        print(line)

def get_expansion_indices(galaxy_map, galaxy_locations):
    width = len(galaxy_map[0])
    height = len(galaxy_map)
    x, y = map(set, zip(*galaxy_locations))
    expand_x = set(range(width)).difference(x)
    expand_y = set(range(height)).difference(y)
    return sorted(expand_x), sorted(expand_y)

def correct_for_cosmic_expansion(galaxy_map, galaxy_locations):
    """
    Duplicates rows and columns which do not contain galaxies.
    """
    expand_x, expand_y = get_expansion_indices(galaxy_map, galaxy_locations)
    new_map = []
    for y in range(len(galaxy_map)):
        row = ""
        for x in range(len(galaxy_map[y])):
            row += galaxy_map[y][x]
            if x in expand_x:
                row += galaxy_map[y][x]
        new_map.append(row)
        if y in expand_y:
            new_map.append(row)
    return new_map

def galaxy_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

class GalaxyDistanceFunctor:
    def __init__(self, expansion_multiplier, indices_x : list, indices_y : list):
        """
        indices_x and indices_y are expected to be sorted lists.
        """
        self.expansion_multiplier = expansion_multiplier
        self.indices_x = indices_x
        self.indices_y = indices_y
    
    def __call__(self, a, b):
        x1 = min(a[0], b[0])
        x2 = max(a[0], b[0])
        y1 = min(a[1], b[1])
        y2 = max(a[1], b[1])
        insert_count_x = bisect.bisect_left(self.indices_x, x2) - bisect.bisect_left(self.indices_x, x1)
        insert_count_y = bisect.bisect_left(self.indices_y, y2) - bisect.bisect_left(self.indices_y, y1)
        #print(insert_count_x, insert_count_y)
        return x2 - x1 + y2 - y1 + (insert_count_x + insert_count_y) * (self.expansion_multiplier - 1)

#content = example.split('\n')
content = open("input.txt").read().split('\n')

#print_content(content)
locations = find_galaxy_locations(content)
#corrected_map = correct_for_cosmic_expansion(content, locations)
expand_x, expand_y = get_expansion_indices(content, locations)
#print_content(corrected_map)
#locations = find_galaxy_locations(corrected_map)
#print(locations)
print("Part 1: ", sum(it.starmap(GalaxyDistanceFunctor(2, expand_x, expand_y), it.combinations(locations, 2))))
print("Part 2: ", sum(it.starmap(GalaxyDistanceFunctor(1000000, expand_x, expand_y), it.combinations(locations, 2))))