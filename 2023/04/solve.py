import math

with open("input.txt") as f:
    foo = []
    for line in f:
        #print(line)
        card, numbers = line.split(":")
        first, second = numbers.split("|")
        first_set = set(first.strip().split(" "))
        second_set = set(second.strip().split(" "))
        in_both_sets = first_set.intersection(second_set)
        if len(in_both_sets) > 0:
            #print(in_both_sets)
            foo.append(int(math.pow(2, len(in_both_sets) - 1)))

    #print(foo)
    print(sum(foo))
