
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




def get_rounds():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-02")

    rounds = []
    with open("input.txt", "r") as file:
        for line in file:
            rounds.append(line[:-1])


    return rounds


def outcome_points(a, b):

    if a == b:
        return 3

    if a == "Rock" and b == "Scissors":
        return 6
    elif a == "Paper" and b == "Rock":
        return 6
    elif a == "Scissors" and b == "Paper":
        return 6

    return 0


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

    score = outcome_points(my_move, their_move)

    return score + SELECTION_BONUS[my_move]



def solve_part1(rounds):


    total = 0
    for round in rounds:
        total += interpret_round(round)

    return total

rounds = get_rounds()

answer1 = solve_part1(rounds)

print(f"part 1 = {answer1}")

