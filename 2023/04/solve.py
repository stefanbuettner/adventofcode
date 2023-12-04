import math
import time

def parse_card_reward_count(line):
    _, numbers = line.split(":")
    first, second = numbers.split("|")
    first_set = set(map(int, filter(lambda s: s != "", first.strip().split(" "))))
    second_set = set(map(int, filter(lambda s: s != "", second.strip().split(" "))))
    return len(first_set.intersection(second_set))

with open("input.txt") as f:
    content = [line.strip() for line in f]
    card_rewards = list(map(parse_card_reward_count, content))
    print("Part 1: ", sum(map(lambda a: int(math.pow(2, a - 1)), filter(lambda r: r > 0, card_rewards))))

    card_counts = [1]*len(content)
    for i in range(0, len(card_counts)):
        new_card_count = card_rewards[i]
        for k in range(i, i + new_card_count):
            card_counts[k + 1] += card_counts[i]
    
    print("Part 2: ", sum(card_counts))
