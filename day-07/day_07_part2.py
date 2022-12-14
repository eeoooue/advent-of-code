

def get_lines():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-07")

    rounds = []
    with open("input.txt", "r") as file:
        for line in file:
            rounds.append(line[:-1])

    return rounds

lines = get_lines()

print(lines)


