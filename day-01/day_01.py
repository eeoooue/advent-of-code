
from filereader import FileReader

array = FileReader.get_lines("01", "input.txt")

food = []
total = 0
for value in array:
    if value == "":
        food.append(total)
        total = 0
    else:
        total += int(value)
food.append(total)

food.sort(reverse=True)

print(f"Part 1 = {food[0]} (75501 for me)")
print(f"Part 2 = {sum(food[:3])} (215594 for me)")
