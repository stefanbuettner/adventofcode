with open("example.txt") as f:
    for line in f:
        card, numbers = line.split(":")
        first, second = numbers.split("|")
        first_set = set(first.split(" "))
        second_set = set(second.split(" "))
        in_both_sets = first_set.intersection(second_set)
        print(line)
