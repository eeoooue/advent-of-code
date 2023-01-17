
from filereader import FileReader
from monkeypen import MonkeyPen

def get_lines(filename):

    return FileReader.get_lines(21, filename)

lines = get_lines("input.txt")

def check_candidate(value):

    pen = MonkeyPen(lines)

    pen.overwrite_value("humn", value)
    pen.overwrite_operator("root", "=")
    pen.solve_all()

    node = pen.nodes["root"]
    a = pen.get_monkey_value(node.one)
    b = pen.get_monkey_value(node.two)

    return int(a-b)

def find_candidate(constant):

    if ans:
        return

    state = ["0"] * 13

    for i in range(13):

        best_score = float("inf")
        best_digit = "0"

        front = "".join(state[:i])
        back = "".join(state[i+1:])

        for d in range(10):
            num = int(f"{front}{d}{back}")
            score = constant * check_candidate(num)

            if score >= 0 and score <= best_score:
                best_score = score
                best_digit = d
        
        state[i] = str(best_digit)

    candidate = int("".join(state))
    if check_candidate(candidate) == 0:
        ans.append(candidate)

ans = []

find_candidate(1)
find_candidate(-1)

if ans:
    print(f"part 2 = {ans[0]} (3469704905529 for me)")
