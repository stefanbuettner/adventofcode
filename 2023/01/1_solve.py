import re

with open("1_input.txt") as f:
    foo = re.compile("\d")
    total = 0
    for line in f:
        matches = foo.findall(line)
        total += 10 * int(matches[0]) + int(matches[-1])
    
    print(total)