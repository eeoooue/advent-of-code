
from filereader import FileReader
from list_class_v2 import MyList

lines = [line for line in FileReader.get_lines(20, "input.txt")]

array = [int(x) for x in lines]



list = MyList(array)


nums = list.get_list_as_arr()



from collections import deque


queue = deque(nums)

while queue[0] != 0:
    x = queue.popleft()
    queue.append(x)

n = len(queue)

puzzle_vals = [1000,2000,3000]

total = 0
for i in puzzle_vals:
    total += queue[i % n]
    #print(f"{i}th val = {queue[i % n]}")

print(f"part 1 ans = {total}")




