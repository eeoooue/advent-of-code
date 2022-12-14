
import os

os.chdir("D:\\GitHub\\advent-of-code\\day-01")

array = []

with open("input.txt", "r") as file:
    for line in file:
        print(line[:-1])
        array.append(line[:-1])
        
print(array)

food = []
total = 0
for value in array:
    if value == "":
        food.append(total)
        total = 0
    else:
        total += int(value)
food.append(total)

most = max(food)

def solve_part1(arr):

    n = len(arr)

    best = 0
    ans = 0
    for i, x in enumerate(arr):
        if x >= best:
            best = x
            ans = i

    

    return best


def solve_part2(food):

    copy = food[:]
    copy.sort()

    print(copy)

    total = 0
    for i in range(3):
        total += copy.pop()

    return total

answer1 = solve_part1(food)

print(f"Part 1 = {answer1}")

answer2 = solve_part2(food)


print(f"Part 2 = {answer2}")




