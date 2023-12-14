example = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

def rotate_content_counterclockwise(content : list):
    new_content = []
    for x in reversed(range(len(content[0]))):
        new_row = ""
        for y in range(len(content)):
            new_row += content[y][x]
        new_content.append(new_row)
    return new_content

def sum_n(n):
    """
    Sum of the numbers from 1 to n
    """
    return n * (n + 1) // 2

def sum_range(i, k):
    """
    Sum of numbers (i, k] with i <= k.
    """
    return sum_n(k) - sum_n(i)

#content = example.split('\n')
content = open("input.txt").read().split('\n')
content = rotate_content_counterclockwise(content)

# At this point moving stones to the left is moving stones north
weight = 0
for row in content:
    row_weight = 0
    left_stone_weight = len(row)
    segments = row.split("#")
    #print(segments)
    for segment in segments:
        segment_length = len(segment)
        num_rolling_stones = segment.count("O")
        assert left_stone_weight >= 0
        row_weight += sum_range(left_stone_weight - num_rolling_stones, left_stone_weight)
        left_stone_weight -= segment_length + 1
    weight += row_weight

print("Part 1: ", weight)