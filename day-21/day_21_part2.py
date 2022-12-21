
from filereader import FileReader

from monkeynode_part2 import MonkeyPen

def get_lines(filename):

    return [line for line in FileReader.get_lines(21, filename)]

lines = get_lines("input.txt")

def solve_attempt(value):

    pen = MonkeyPen()

    pen.interpret_array(lines)

    pen.overwrite_value("humn", value)
    pen.overwrite_operator("root", "=")
    pen.solve_all()

    node = pen.nodes["root"]

    a = pen.values[node.one]
    b = pen.values[node.two]

    print(f"({int(a-b)}) {int(abs(a-b))} (dist from value = {value}) || {a} needs to equal {b}")

    return int(a-b)

state = ["0"] * 13

for i in range(13):

    best_score = float("inf")
    best_digit = "0"

    state_str = "".join(state)
    front = state_str[:i]
    back = state_str[i+1:]

    for d in "0123456789":

        num = int(f"{front}{d}{back}")
        score = solve_attempt(num)

        if score >= 0 and score <= best_score:
            best_score = score
            best_digit = d
    
    state[i] = best_digit

part2_ans = "".join(state)

print(f"part 2 = {part2_ans} (3469704905529 for me)")