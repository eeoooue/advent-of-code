# advent-of-code/2022/day02
from enum import Enum


class FileReader:
    @staticmethod
    def get_lines(filename):
        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


class MoveOption(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2


class RockPaperScissors:
    @staticmethod
    def interpret_round(my_move, their_move):
        score = RockPaperScissors.outcome_points(my_move, their_move)
        score += my_move.value + 1

        return score

    @staticmethod
    def outcome_points(a: MoveOption, b: MoveOption):
        offset = (b.value - a.value) % 3

        match offset:
            case 0:
                return 3
            case 1:
                return 0
            case 2:
                return 6


class Solution:
    def __init__(self, lines) -> None:
        self.rounds = lines

        self.moves = {
            "A": MoveOption.Rock,
            "B": MoveOption.Paper,
            "C": MoveOption.Scissors,
            "X": MoveOption.Rock,
            "Y": MoveOption.Paper,
            "Z": MoveOption.Scissors,
        }

    def get_total_from_strategy(self, puzzle_part):
        total = 0
        for line in self.rounds:
            (their_move, my_move) = self.unpack_moves(line, puzzle_part)
            total += RockPaperScissors.interpret_round(my_move, their_move)

        return total

    def unpack_moves(self, line, part):
        (a, b) = line.split(" ")
        their_move = self.moves[a]

        if part == 1:
            my_move = self.moves[b]
        else:
            my_move = self.find_suggested_move(their_move, b)

        return (their_move, my_move)

    def find_suggested_move(self, their_move: MoveOption, instruction):
        winning_value = (their_move.value - 2) % 3
        losing_value = (their_move.value - 1) % 3

        match instruction:
            case "X":
                return MoveOption(losing_value)
            case "Y":
                return MoveOption(their_move.value)
            case "Z":
                return MoveOption(winning_value)


rounds = FileReader.get_lines("input.txt")
solver = Solution(rounds)

ans_part_1 = solver.get_total_from_strategy(1)
ans_part_2 = solver.get_total_from_strategy(2)

print(f"My total score after all move pairs would be {ans_part_1}.")
print(f"My total score after following the instructions would be {ans_part_2}.")
