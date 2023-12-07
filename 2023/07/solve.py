import re

class HandBid:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
    
    def __repr__(self):
        return "({}, {})".format(self.hand, self.bid)

def line_to_handbid(line):
    hand, bid = line.split(" ")
    return HandBid(hand, int(bid))

card_ranks = "23456789TJQKA"

def card_rank(handbid):
    # Lists in python compare lexicographically
    # So transforming the hand into a list of indices
    # into the list of the rank of the cards will
    # serve as a key for sorting handbids by card_rank
    #print(list(map(card_ranks.index, handbid.hand)))
    return list(map(card_ranks.index, handbid.hand))

def hand_type(handbid):
    sorted_hand = "".join(sorted(handbid.hand))
    print(sorted_hand)
    # 2{4}|3{4}|...|A{4}
    five_of_a_kind = re.compile("{5}|".join(card_ranks)+"{5}")
    if five_of_a_kind.search(sorted_hand):
        print("five_of_a_kind")
        return 7
    four_of_a_kind = re.compile("{4}|".join(card_ranks)+"{4}")
    if four_of_a_kind.search(sorted_hand):
        print("four_of_a_kind")
        return 6
    #full_house = re.compile()
    return 0

with open("example.txt") as f:
    handbids = list(map(line_to_handbid, f))
    handbids.sort(key=card_rank)
    handbids.sort(key=hand_type)
    print(handbids)
    