import re

digit_word_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 

def parse_match_to_int(match):
    try:
        return int(match)
    except:
        return digit_word_to_int[match]

def find_first_of(text, matches):
    indices = [text.find(match) for match in matches]
    # print(indices)
    min_idx = min(idx for idx in indices if idx > -1)
    # print(min_idx)
    try:
        match_idx = indices.index(min_idx)
        return matches[match_idx]
    except:
        return None

def find_last_of(text, matches):
    indices = [text.rfind(match) for match in matches]
    # print(indices)
    max_idx = max(idx for idx in indices if idx > -1)
    # print(max_idx)
    try:
        match_idx = indices.index(max_idx)
        return matches[match_idx]
    except:
        return None

with open("2_input.txt") as f:
    total = 0
    for line in f:
        first_match = find_first_of(line, digits)
        second_match = find_last_of(line, digits)
        # print(first_match)
        # print(second_match)
        if (first_match != second_match) and ((first_match == None) or (second_match == None)):
            raise RuntimeError("Uhoh")
        if first_match == None:
            continue
        total += 10 * parse_match_to_int(first_match) + parse_match_to_int(second_match)
    
    print(total)