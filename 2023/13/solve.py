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
        mirror_check_range = min(lower_horizontal_mirror_idx + 1, len(pattern) - lower_horizontal_mirror_idx - 1)
        num_characters_different = 0
        for y in range(mirror_check_range):
            for c in range(len(pattern[lower_horizontal_mirror_idx - y])):
                if pattern[lower_horizontal_mirror_idx - y][c] != pattern[lower_horizontal_mirror_idx + y + 1][c]:
                    num_characters_different += 1
                    if num_characters_different > 1:
                        break
            if num_characters_different > 1:
                break
        #print(lower_horizontal_mirror_idx, num_cols_different)
        if num_characters_different == 1:
            return lower_horizontal_mirror_idx + 1
    return None

def find_vertical_mirror(pattern : list):
    for lower_vertical_mirror_idx in range(len(pattern[0]) - 1):
        mirror_check_range = min(lower_vertical_mirror_idx + 1, len(pattern[0]) - lower_vertical_mirror_idx - 1)
        num_characters_different = 0
        for x in range(mirror_check_range):
            for y in range(len(pattern)):
                if pattern[y][lower_vertical_mirror_idx - x] != pattern[y][lower_vertical_mirror_idx + x + 1]:
                    num_characters_different += 1
                    if num_characters_different > 1:
                        break
            if num_characters_different > 1:
                break
        if num_characters_different == 1:
            return lower_vertical_mirror_idx + 1
    return None

#content = list(map(lambda p: p.split('\n'), example.split('\n\n')))
content = list(map(lambda p: p.split('\n'), open("input.txt").read().split('\n\n')))

vertical_mirrors = filter(None, map(find_vertical_mirror, content))
#print(vertical_mirrors)
horizontal_mirrors = filter(None, map(find_horizontal_mirror, content))
#print(horizontal_mirrors)
print("Part 2: ", sum(vertical_mirrors) + 100 * sum(horizontal_mirrors))