
from filereader import FileReader
from rockpaperscissors import RockPaperScissors

MOVE_LOOK = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

SELECTION_BONUS = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

def get_winning_move(them):

    if them == "Rock":
        return "Paper"

    if them == "Paper":
        return "Scissors"
    
    if them == "Scissors":
        return "Rock"

def get_losing_move(them):

    if them == "Rock":
        return "Scissors"

    if them == "Paper":
        return "Rock"
    
    if them == "Scissors":
        return "Paper"

def interpret_round(round):

    their_move = MOVE_LOOK[round[0]]
    my_move = ""

    instruction = round[2]
    
    if instruction == "X":
        my_move = get_losing_move(their_move)
    elif instruction == "Y":
        my_move = their_move
    else:
        my_move = get_winning_move(their_move)

    score = RockPaperScissors.outcome_points(my_move, their_move)

    return score + SELECTION_BONUS[my_move]

def solve_part2(rounds):

    total = 0
    for round in rounds:
        total += interpret_round(round)

    return total

rounds = FileReader.get_lines("02", "input.txt")

print(f"part 2 = {solve_part2(rounds)} (10398 for me)")

