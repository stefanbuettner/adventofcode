import re
import itertools as it

example = """#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1"""

one_damaged_example = """???.### 1,1,3"""

damaged_example = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

def parse_row(row):
    record, s_parity_list = row.split(' ')
    parity_list = map(int, s_parity_list.split(","))
    return record, list(parity_list)

#foo = re.compile("(\.+)|(#+)")
def record_to_parity_list(record):
    parity_list = [len(list(g)) for k, g in it.groupby(record) if k == "#"]
    return parity_list

def generate_possibilities(record : str):
    # First replace all the adjacent
    unknown_quality_count = record.count("?")
    print(2**unknown_quality_count)
    for foo in it.product(".#", repeat=unknown_quality_count):
        possibility = ""
        k = 0
        for i in range(len(record)):
            if record[i] == "?":
                possibility += foo[k]
                k += 1
            else:
                possibility += record[i]
        yield possibility

#content = example.split('\n')
#content = damaged_example.split('\n')
content = open("input.txt").read().split('\n')

records, parity_lists = zip(*map(parse_row, content))
# print(list(map(generate_possibilities, records)))
mus = 0
for i in range(len(records)):
    mus += sum(1 for _ in filter(lambda p: p == parity_lists[i], map(record_to_parity_list, generate_possibilities(records[i]))))
    #print()
    # for possibility in generate_possibilities(record):
    #     pass
print("Part 1: ", mus)
# p = tuple(map(record_to_parity_list, records))
# print(type(parity_lists))
# print(type(p))
# print(parity_lists)
# print(p)