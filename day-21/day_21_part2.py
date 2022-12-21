
from filereader import FileReader
from monkeypen import MonkeyPen

def get_lines(filename):

    return [line for line in FileReader.get_lines(21, filename)]

lines = get_lines("input.txt")

def solve_a_minus_b(value):

    pen = MonkeyPen()

    pen.interpret_array(lines)

    pen.overwrite_value("humn", value)
    pen.overwrite_operator("root", "=")
    pen.solve_all()

    node = pen.nodes["root"]

    a = pen.values[node.one]
    b = pen.values[node.two]

    return int(a-b)

def solve_b_minus_a(value):

    pen = MonkeyPen()

    pen.interpret_array(lines)

    pen.overwrite_value("humn", value)
    pen.overwrite_operator("root", "=")
    pen.solve_all()

    node = pen.nodes["root"]

    a = pen.values[node.one]
    b = pen.values[node.two]

    return int(b-a)



def look_direction_1():

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
            score = solve_a_minus_b(num)

            if score >= 0 and score <= best_score:
                best_score = score
                best_digit = d
        
        state[i] = str(best_digit)

    candidate = int("".join(state))
    if solve_a_minus_b(candidate) == 0:
        ans.append(candidate)

def look_direction_2():

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
            score = solve_b_minus_a(num)

            if score >= 0 and score <= best_score:
                best_score = score
                best_digit = d
        
        state[i] = str(best_digit)

    candidate = int("".join(state))
    if solve_a_minus_b(candidate) == 0:
        ans.append(candidate)

ans = []

look_direction_1()
look_direction_2()

print(ans)
