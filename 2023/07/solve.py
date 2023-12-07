import re
import itertools as it
import operator as op

class HandBid:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
    
    def __repr__(self):
        return "({}, {})".format(self.hand, self.bid)

def line_to_handbid(line):
    hand, bid = line.split(" ")
    return HandBid(hand, int(bid))

card_ranks = "J23456789TQKA"

def card_rank(handbid):
    # Lists in python compare lexicographically
    # So transforming the hand into a list of indices
    # into the list of the rank of the cards will
    # serve as a key for sorting handbids by card_rank
    return list(map(card_ranks.index, handbid.hand))

def normalize_hand(hand : str):
    """
    Maps the most common card to a, the second most common card to b, etc.
    This allows to determine the hand type more easily.
    """
    joker_count = hand.count("J")
    if joker_count >= 5:
        return "a"*joker_count
    cards = set(list(hand))
    if joker_count > 0:
        cards.remove("J")
    card_counts = sorted(list(map(hand.count, cards)), reverse=True)
    if joker_count > 0:
        card_counts[0] += joker_count
    normalized_card_ids = list("abcde")
    return "".join(map(op.mul, normalized_card_ids, card_counts))

def hand_type(handbid):
    normalized_hand = normalize_hand(handbid.hand)
    # five_of_a_kind
    if re.search("a{5}", normalized_hand):
        return 7
    # four_of_a_kind
    if re.search("a{4}", normalized_hand):
        return 6
    # full_house
    if re.search("a{3}b{2}", normalized_hand):
        return 5
    # three_of_a_kind 
    if re.search("a{3}", normalized_hand):
        return 4
    # two_pair
    if re.search("a{2}b{2}", normalized_hand):
        return 3
    # one_pair
    if re.search("a{2}", normalized_hand):
        return 2
    return 1

def solve(content : list):
    handbids = list(map(line_to_handbid, content))
    handbids.sort(key=card_rank)
    handbids.sort(key=hand_type)
    # [(bid, 1), (bid, 2), ...]
    bids_and_weights = enumerate(map(lambda handbid: handbid.bid, handbids), start=1)
    return sum(it.starmap(op.mul, bids_and_weights))

with open("input.txt") as f:
    content = [line for line in f]
    print(solve(content))
    