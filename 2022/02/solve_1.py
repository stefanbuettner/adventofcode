rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]

# loss = "X"
# draw = "Y"
# win = "Z"

def round_score(opponent_move, own_move):
    if opponent_move in rock and own_move in rock:
        return 3
    elif opponent_move in rock and own_move in paper:
        return 6
    elif opponent_move in rock and own_move in scissors:
        return 0
    elif opponent_move in paper and own_move in rock:
        return 0
    elif opponent_move in paper and own_move in paper:
        return 3
    elif opponent_move in paper and own_move in scissors:
        return 6
    elif opponent_move in scissors and own_move in rock:
        return 6
    elif opponent_move in scissors and own_move in paper:
        return 0
    elif opponent_move in scissors and own_move in scissors:
        return 3

# def required_move(opponent_move, result):
#     if opponent_move == rock and result = loss
#         return 

def move_score(move):
    if move in rock:
        return 1
    elif move in paper:
        return 2
    elif move in scissors:
        return 3

with open("input.txt") as f:
    moves = map(str.split, f)
    opponent_moves, own_moves = map(list, zip(*moves))
    total_score = sum(map(round_score, opponent_moves, own_moves) + map(move_score, own_moves))
    print("Total score: {}".format(total_score))