example = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

def find_horizontal_mirror(pattern : list):
    for lower_horizontal_mirror_idx in range(len(pattern) - 1):
        mirror_idx_found = True
        mirror_check_range = min(lower_horizontal_mirror_idx + 1, len(pattern) - lower_horizontal_mirror_idx - 1)
        for y in range(mirror_check_range):
            if pattern[lower_horizontal_mirror_idx - y] != pattern[lower_horizontal_mirror_idx + y + 1]:
                mirror_idx_found = False
                break
        if mirror_idx_found:
            return lower_horizontal_mirror_idx + 1
    return None

def find_vertical_mirror(pattern : list):
    for lower_vertical_mirror_idx in range(len(pattern[0]) - 1):
        mirror_idx_found = True
        mirror_check_range = min(lower_vertical_mirror_idx + 1, len(pattern[0]) - lower_vertical_mirror_idx - 1)
        for x in range(mirror_check_range):
            columns_equal = True
            for y in range(len(pattern)):
                if pattern[y][lower_vertical_mirror_idx - x] != pattern[y][lower_vertical_mirror_idx + x + 1]:
                    columns_equal = False
                    break
            if not columns_equal:
                mirror_idx_found = False
                break
        if mirror_idx_found:
            return lower_vertical_mirror_idx + 1
    return None

#content = list(map(lambda p: p.split('\n'), example.split('\n\n')))
content = list(map(lambda p: p.split('\n'), open("input.txt").read().split('\n\n')))

vertical_mirrors = filter(None, map(find_vertical_mirror, content))
horizontal_mirrors = filter(None, map(find_horizontal_mirror, content))
print("Part 1: ", sum(vertical_mirrors) + 100 * sum(horizontal_mirrors))