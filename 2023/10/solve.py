import itertools as it

simple_loop = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

example_loop = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

example_enclosing_1 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

example_enclosing_2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

example_enclosing_3 = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""

def get_element(pipe_map, x, y):
    """
    Returns "X" outside of the given map.
    This simplifies some checks because no explicit "is not None" check is needed.
    """
    if y < 0 or x < 0 or len(pipe_map) <= y:
        return "X"
    if len(pipe_map[y]) <= x:
        return "X"
    return pipe_map[y][x]

def print_pipe_map(pipe_map):
    for line in pipe_map:
        foo = ""
        for x in line:
            foo += x["type"]
        print(foo)
    print()

NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

# These direction result in a counter-clockwise traversal of the resulting loop
# due to the stack nature of the loop finding algorithm.
directions = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
    ".": [],
    "S": [NORTH, EAST, SOUTH, WEST],
}

def direction_to_step(direction):
    if direction == NORTH:
        return (0, -1)
    if direction == EAST:
        return (1, 0)
    if direction == SOUTH:
        return (0, 1)
    if direction == WEST:
        return (-1, 0)

def step_to_direction(step):
    if step == (0, -1):
        return NORTH
    if step == (1, 0):
        return EAST
    if step == (0, 1):
        return SOUTH
    if step == (-1, 0):
        return WEST

opposite_direction = {
    NORTH: SOUTH,
    EAST: WEST,
    SOUTH: NORTH,
    WEST: EAST,
}

def compute_loop_nodes(pipe_map, start_coordinates):
    """
    Returns the loop nodes as a list. When traversing the list front to back
    the loop is traveresed counter-clockwise.

    [(x, y), ...]
    """
    loop_nodes = []
    queue = [(start_coordinates, None)] # ((x, y), incoming_direction)
    while len(queue) > 0:
        (curr_x, curr_y), incoming_direction = queue.pop()
        current_element = get_element(pipe_map, curr_x, curr_y)
        if current_element["visited"]:
            # Found loop
            return loop_nodes
        loop_nodes.append((curr_x, curr_y))
        current_element["visited"] = True
        edge_type = current_element["type"]
        took_step = False
        for direction in directions[edge_type]:
            # Don't go where we came from
            if opposite_direction[direction] == incoming_direction:
                continue
            dx, dy = direction_to_step(direction)
            x = curr_x + dx
            y = curr_y + dy
            next_element = get_element(pipe_map, x, y)
            if next_element == "X":
                continue
            # Only go if the next node has an edge to this node
            if opposite_direction[direction] in next_element["edges"]:
                took_step = True
                queue.append(((x, y), direction))
        if not took_step:
            loop_nodes.pop()
    assert False


def compute_pipe_map(content):
    """
    Generates the pipe_map based on the file content.

    Returns the pipe_map and the start coordinates
    """
    width = len(content[0])
    height = len(content)
    pipe_map = [[{"edges" : list(), "distance": None, "visited": False, "type": "."} for _ in range(width)] for _ in range(height)]
    start_coordinates = None
    for y in range(height):
        for x in range(width):
            edge_type = content[y][x]
            pipe_map[y][x]["type"] = edge_type
            pipe_map[y][x]["edges"] = directions[edge_type]
            if edge_type == "S":
                start_coordinates = (x, y)
    return pipe_map, start_coordinates

def node_difference(a, b):
    return (a[0] - b[0], a[1] - b[1])

# Directions are out-going directions
type_direction_to_inner_offset = {
    "|": {
        NORTH: [direction_to_step(WEST)],
        SOUTH: [direction_to_step(EAST)],
    },
    "-": {
        EAST: [direction_to_step(NORTH)],
        WEST: [direction_to_step(SOUTH)],
    },
    "L": {
        EAST: [],
        NORTH: [direction_to_step(SOUTH), direction_to_step(WEST)],
    },
    "J": {
        NORTH: [],
        WEST: [direction_to_step(EAST), direction_to_step(SOUTH)],
    },
    "7": {
        WEST: [],
        SOUTH: [direction_to_step(NORTH), direction_to_step(EAST)],
    },
    "F": {
        EAST: [direction_to_step(WEST), direction_to_step(NORTH)],
        SOUTH: [],
    },
}

# Used for determining the type of S based on the
# first and last loop node.
directions_to_type = {
    (NORTH, NORTH): "|",
    (NORTH, EAST): "F",
    (NORTH, WEST): "7",
    (EAST, NORTH): "J",
    (EAST, EAST): "-",
    (EAST, SOUTH): "7",
    (SOUTH, SOUTH): "|",
    (SOUTH, EAST): "L",
    (SOUTH, WEST): "J",
    (WEST, NORTH): "L",
    (WEST, SOUTH): "F",
    (WEST, WEST): "-",
}

corner_nodes = "F7JL"
corner_is_changing_side = {
    "F": {
        "J": True,
        "7": False,
    },
    "L": {
        "J": False,
        "7": True,
    }
}

def find_inner_nodes(pipe_map, loop):
    """
    Loop is assumed to wind counter-lockwise.
    See comment of the directions-map.

    Returns a list of inner nodes: [(x, y), ...]
    """
    directions = list(map(step_to_direction, map(node_difference , loop[1:], loop[:-1])))
    directions.append(step_to_direction(node_difference(loop[0], loop[-1])))
    #print(directions)
    inner_nodes = []
    loop_directions = {node: direction for node, direction in it.zip_longest(loop, directions)}
    # print(loop_directions)

    y = 0
    for row in pipe_map:
        x = 0
        inside = False
        first_corner = None
        for node in row:
            # If we hit the loop
            if (x, y) in loop_directions:
                t = node["type"]
                if t == "S":
                    t = directions_to_type[(directions[-1], directions[0])]
                # If we hit a corner of the loop
                # this means that we're dealing with a horizontal segment.
                # They can either change the side or not:
                #
                # II|OOO  IIIIII
                # IIL-7O  IIF7II
                # IIII|O  II||II
                #
                # Also corners always come in pairs.
                # Therfore we need to save the first corner and act with
                # that when encountering the second corner.
                if t in corner_nodes:
                    if first_corner is None:
                        first_corner = t
                    else:
                        if corner_is_changing_side[first_corner][t]:
                            inside = not inside
                        first_corner = None
                # Vertical walls always change the side
                elif t == "|":
                    inside = not inside
            # If it's not a node on the loop it's either inside or outside.
            elif inside:
                inner_nodes.append((x, y))
            x += 1
        y += 1
    return inner_nodes

#content = simple_loop.split('\n')
#content = example_loop.split('\n')
#content = example_enclosing_1.split('\n') # 4
#content = example_enclosing_2.split('\n') # 10
#content = example_enclosing_3.split('\n') # 4
content = open("input.txt").read().split('\n')
pipe_map, start_coordinates = compute_pipe_map(content)
# print_pipe_map(pipe_map)
loop_nodes = compute_loop_nodes(pipe_map, start_coordinates)
print("Part 1: ", int((len(loop_nodes)) / 2))
print("Part 2: ", len(find_inner_nodes(pipe_map, loop_nodes)))
