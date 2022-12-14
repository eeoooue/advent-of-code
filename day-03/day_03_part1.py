
def get_lines():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-03")

    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append(line[:-1])

    return lines



def split_halfway(s):

    n = len(s)
    i = n//2

    a = s[:i]
    b = s[i:]

    return [a, b]

def get_common_elements(arr):

    pool = set(arr[0])
    for s in arr:
        new = set([])
        for x in s:
            if x in pool:
                new.add(x)
        pool = new

    for x in pool:
        return x

def get_lookup():

    ABC = "abcdefghijklmnopqrstuvwxyz"

    points = {}
    i = 0
    for x in ABC:
        i += 1
        points[x] = i
    
    for x in ABC.upper():
        i += 1
        points[x] = i

    return points


lines = get_lines()
points = get_lookup()

total = 0
for line in lines:
    arr = split_halfway(line)
    x = get_common_elements(arr)
    total += points[x]

print(f"part 1 = {total}")




n = len(lines)

total = 0
i = 0
arr = []
while i < n:
    arr.append(lines[i])
    i += 1

    if len(arr) == 3:
        print(arr)
        x = get_common_elements(arr)
        total += points[x]
        arr = []

print(f"part 2 = {total}")