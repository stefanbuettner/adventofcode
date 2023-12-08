import re
import itertools as it
import math

def num_steps(node_map : dict, start_node, instructions : str, terminal_condition):
    instruction = it.cycle(instructions)
    current_node = start_node
    steps = 0
    while not terminal_condition(current_node):
       current_instruction = next(instruction)
       current_node = node_map[current_node][current_instruction]
       steps += 1
    return steps

with open("input.txt") as f:
    node_map = {}
    instructions = ""
    node_regex = re.compile("([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)")
    start_nodes = []
    for line in f:
        line = line.strip()
        match = node_regex.match(line)
        if match:
            node = match.group(1)
            left = match.group(2)
            right = match.group(3)
            node_map[node] = {"L": left, "R": right}
            if node.endswith("A"):
                start_nodes.append(node)
        elif len(line) > 0:
            instructions = line

    print("Part 1: ", num_steps(node_map, "AAA", instructions, lambda node: node == "ZZZ"))    

    steps = list(map(lambda node: num_steps(node_map, node, instructions, lambda node: node.endswith("Z")), start_nodes))
    print("Part 2: ", math.lcm(*steps))
