
class RockPaperScissors:

    @staticmethod
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
