

def get_lines():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-04")

    rounds = []
    with open("input.txt", "r") as file:
        for line in file:
            rounds.append(line[:-1])


    return rounds

lines = get_lines()

#lines = [
#    "2-4,6-8",
#    "2-3,4-5",
#    "5-7,7-9",
#    "2-8,3-7",
#    "6-6,4-6",
#    "2-6,4-8",
#]


def interpret_range(rangestring):

    i = rangestring.index("-")

    front = int(rangestring[:i])
    end = int(rangestring[i+1:])

    return (front, end)

def a_contains_b(a, b):

    (a_front, a_end) = interpret_range(a)
    (b_front, b_end) = interpret_range(b)

    if a_front <= b_front:
        if a_end >= b_end:
            return True

def a_overlaps_b(a, b):

    (a_front, a_end) = interpret_range(a)
    (b_front, b_end) = interpret_range(b)

    if a_front <= b_front:
        if a_end >= b_end:
            return True

    if a_front <= b_front and a_end >= b_front:
        return True

def p1_criteria_met(line):


    arr = line.split(",")
    a = arr[0]
    b = arr[1]

    if a_contains_b(a, b) or a_contains_b(b, a):
        return True

    return False


def p2_criteria_met(line):


    arr = line.split(",")
    a = arr[0]
    b = arr[1]

    if a_overlaps_b(a, b) or a_overlaps_b(b, a):
        return True

    return False

def solve_part1(array):


    count = 0
    for line in array:
        if p1_criteria_met(line):
            count += 1

    return count

def solve_part2(array):


    count = 0
    for line in array:
        if p2_criteria_met(line):
            count += 1

    return count

part1_ans = solve_part1(lines)
print(f"part 1: {part1_ans}")

part2_ans = solve_part2(lines)
print(f"part 2: {part2_ans}")