
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

def interpret_round(round):

    their_move = MOVE_LOOK[round[0]]
    my_move = MOVE_LOOK[round[2]]

    score = RockPaperScissors.outcome_points(my_move, their_move)

    return score + SELECTION_BONUS[my_move]

def solve_part1(rounds):

    total = 0
    for round in rounds:
        total += interpret_round(round)

    return total

rounds = FileReader.get_lines("02", "input.txt")

print(f"part 1 = {solve_part1(rounds)} (13009 for me)")

