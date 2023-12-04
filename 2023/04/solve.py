import math
import time

def parse_card_reward_count(line):
    _, numbers = line.split(":")
    first, second = numbers.split("|")
    first_set = set(map(int, filter(lambda s: s != "", first.strip().split(" "))))
    second_set = set(map(int, filter(lambda s: s != "", second.strip().split(" "))))
    return len(first_set.intersection(second_set))

def part1(line):
    count = parse_card_reward_count(line)
    if count <= 0:
        return 0
    return int(math.pow(2, count - 1))


# {nr: count, ...}
card_rewards = {}
# Card numbers, 1 based
card_queue = []

with open("input.txt") as f:
    foo = []
    content = [line.strip() for line in f]
    for line in content:
        foo.append(part1(line))

    print("Part 1: ", sum(foo))
    
    card_queue = list(range(1, len(content) + 1))
    number_cards_won = 0
    while len(card_queue) > 0:
        #print(card_queue)
        number_cards_won += 1
        card_nr = card_queue.pop(0)
        if card_nr not in card_rewards:
            card_reward_count = parse_card_reward_count(content[card_nr - 1])
            card_rewards[card_nr] = card_reward_count
        else:
            card_reward_count = card_rewards[card_nr]
        card_queue.extend([card_nr + 1 + k for k in range(0, card_reward_count)])
        #time.sleep(0.5)
    
    print("Part 2: ", number_cards_won)
