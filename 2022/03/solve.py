def item_priority(char):
    if ord('a') <= ord(char) and ord(char) <= ord('z'):
        return ord(char) - ord('a') + 1
    if ord('A') <= ord(char) and ord(char) <= ord('Z'):
        return ord(char) - ord('A') + 27
    raise RuntimeError("Invalid item: " + char)

with open("input.txt") as f:
    sum_priorities = 0
    for rucksack in f:
        rucksack = rucksack.strip()
        mid = len(rucksack) / 2
        assert mid * 2 == len(rucksack)
        comp1 = rucksack[0:mid]
        comp2 = rucksack[mid:]
        # print(comp1)
        # print(comp2)
        comp1 = set(comp1)
        comp2 = set(comp2)
        # print(comp1)
        # print(comp2)
        common_items = comp1.intersection(comp2)
        # print(common_items)
        assert len(common_items) == 1
        sum_priorities += item_priority(common_items.pop())
    
    print("Sum priorities: {}".format(sum_priorities))