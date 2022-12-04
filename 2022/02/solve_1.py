rock = "A"
paper = "B"
scissors = "C"

loss = "X"
draw = "Y"
win = "Z"

def round_score(opponent_move, own_move):
    if opponent_move == rock and own_move == rock:
        return 3
    elif opponent_move == rock and own_move == paper:
        return 6
    elif opponent_move == rock and own_move == scissors:
        return 0
    elif opponent_move == paper and own_move == rock:
        return 0
    elif opponent_move == paper and own_move == paper:
        return 3
    elif opponent_move == paper and own_move == scissors:
        return 6
    elif opponent_move == scissors and own_move == rock:
        return 6
    elif opponent_move == scissors and own_move == paper:
        return 0
    elif opponent_move == scissors and own_move == scissors:
        return 3

def required_move(opponent_move, result):
    if result == draw:
        return opponent_move
    if result == loss:
        if opponent_move == rock:
            return scissors
        elif opponent_move == paper:
            return rock
        elif opponent_move == scissors:
            return paper
    if result == win:
        if opponent_move == rock:
            return paper
        elif opponent_move == paper:
            return scissors
        elif opponent_move == scissors:
            return rock

def move_score(move):
    if move in rock:
        return 1
    elif move in paper:
        return 2
    elif move in scissors:
        return 3

with open("input.txt") as f:
    moves = map(str.split, f)
    opponent_moves, desired_result = map(list, zip(*moves))
    own_moves = map(required_move, opponent_moves, desired_result)
    total_score = sum(map(round_score, opponent_moves, own_moves) + map(move_score, own_moves))
    print("Total score: {}".format(total_score))