import itertools as it
import operator as op

def generate_triangle(line : str):
    """
    Generates the triangle of differences, e.g.
    0   3   6   9  12  15
      3   3   3   3   3
        0   0   0   0
    """
    history = list(map(int, line.strip().split(" ")))
    triangle = [history]
    for i in range(0, len(history)):
        triangle.append(list(map(op.sub, triangle[i][1:], triangle[i][0:-1])))
        if all(entry == 0 for entry in triangle[-1]):
            break
    return triangle

def predict_next_value(triangle : list):
    last_idx = len(triangle) - 1
    next_value = 0
    for k in range(0, len(triangle)):
        next_value = triangle[last_idx - k][-1] + next_value
    return next_value

def predict_previous_value(triangle : list):
    last_idx = len(triangle) - 1
    previous_value = 0
    for k in range(0, len(triangle)):
        previous_value = triangle[last_idx - k][0] - previous_value
    return previous_value

with open("input.txt") as f:
    content = [line.strip() for line in f]
    triangles = list(map(generate_triangle, content))
    print("Part 1: ", sum(map(predict_next_value, triangles)))
    print("Part 2: ", sum(map(predict_previous_value, triangles)))