import re
import itertools as it
import math

example = """#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1"""

#one_damaged_example = """???.### 1,1,3"""
one_damaged_example = """?????.?##???..??? 1,3"""

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

def binomial(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

def analyze_record(record, parity_list):
    # print(record, parity_list)
    unknown_quality_count = record.count("?")
    unknown_possibilities = 2**unknown_quality_count

    # Dots are separated by the ###
    # Thus, the number of ways to combine the free dots (zeros) with the ### (ones)
    # is binomial(n + k, k)
    # https://en.wikipedia.org/wiki/Binomial_coefficient#Combinatorics_and_statistics
    k = len(parity_list)
    sum_parity = sum(parity_list)
    len_record = len(record)
    num_dots = len_record - sum_parity
    free_dots = num_dots - (k - 1)
    valid_records = binomial(free_dots + k, k)

    return unknown_possibilities, valid_records, free_dots, k

def next_ones_zeros(s : str):
    """
    0000111
    0001011
    0001101
    0001110
    0010011
    0010101
    0010110
    0011001
    0011010
    ...
    1110000
    """
    #s = "".join(l)
    sr = "".join(reversed(s))
    first_10 = sr.find("10")
    if first_10 < 0:
        # We got the last combination as input
        return s
    last_01 = len(s) - first_10 - 2
    next_l = s[0:last_01] + "10"
    if s.count("1", last_01) - 1 > 0:
        trailing_zeros = s.count("0", last_01) - 1
        next_l += "0" * trailing_zeros
        next_l += "1" * (len(s) - last_01 - 2 - trailing_zeros)
    else:
        next_l += s[last_01 + 2:]
    return next_l

def generate_zeros_ones(k_zeros, n_ones):
    v = "0" * k_zeros + "1" * n_ones
    yield v
    w = next_ones_zeros(v)
    while w != v:
        yield w
        v = w
        w = next_ones_zeros(v)
    return

def generate_possibilities_2(record, parity_list):
    # print(record, parity_list)
    # unknown_quality_count = record.count("?")
    # unknown_possibilities = 2**unknown_quality_count

    # Dots are separated by the ###
    # Thus, the number of ways to combine the free dots (zeros) with the ### (ones)
    # is binomial(n + k, k)
    # https://en.wikipedia.org/wiki/Binomial_coefficient#Combinatorics_and_statistics
    # k = len(parity_list)
    # sum_parity = sum(parity_list)
    # len_record = len(record)
    # num_dots = len_record - sum_parity
    # free_dots = num_dots - (k - 1)
    
    #valid_records = binomial(free_dots + k, k)
    _, _, free_dots, k = analyze_record(record, parity_list)

    s = set(generate_zeros_ones(free_dots, k))
    #print(len(s), valid_records)

    for t in s:
        #print(t)
        possibility = ""
        i = 0
        for c in t:
            if c == "0":
                possibility += "."
            elif c == "1":
                possibility += "#" * parity_list[i]
                i += 1
                if i < len(parity_list):
                    possibility += "."
            else:
                assert False
        matching_possibility = True
        for k in range(len(record)):
            if record[k] != "?":
                if record[k] != possibility[k]:
                    matching_possibility = False
                    break
        if matching_possibility:
            yield possibility

#content = example.split('\n')
#content = damaged_example.split('\n')
#content = one_damaged_example.split('\n')
content = open("input.txt").read().split('\n')

records, parity_lists = zip(*map(parse_row, content))
records_and_parity = zip(records, parity_lists)

# print(list(map(generate_possibilities, records)))
mus = 0
for i in range(len(records)):
    #mus += sum(1 for _ in filter(lambda p: p == parity_lists[i], map(record_to_parity_list, generate_possibilities(records[i]))))
    unknown_possibilities, valid_records, _, _ = analyze_record(records[i], parity_lists[i])
    #print(records[i], unknown_possibilities, valid_records)
    mus += sum(1 for _ in generate_possibilities_2(records[i], parity_lists[i]))
    #print()
    # for possibility in generate_possibilities(record):
    #     pass
print("Part 1: ", mus)

# for c in [(2, 3), (7, 9), (9, 7), (1, 5), (0, 0), (0, 5), (5, 0)]:
#     f = list(generate_zeros_ones(*c))
#     assert binomial(c[0] + c[1], c[1]) == len(f)


# for s in generate_zeros_ones(3, 3):
#     print(s)
#print("Part 1: ", sum(map(lambda i: len(list(i)), it.starmap(generate_possibilities_2, records_and_parity))))


#possibilities = sorted(it.starmap(generate_possibilities_2, records_and_parity), key=lambda a: a[1])
# print("Max unknowns: ", max(possibilities, key=lambda a: a[1]))
# print("Max valid: ", max(possibilities, key=lambda a: a[2]))