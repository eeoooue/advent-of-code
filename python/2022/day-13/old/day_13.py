
from filereader import FileReader

pairs = [line for line in FileReader.get_lines(13, "example.txt") if len(line) > 1]

print(pairs)

DIGITS = set("0123456789")


def unpack(s):

    nums = []

    stack = []
    for x in s:
        if x not in DIGITS:
            if stack:
                nums.append(int("".join(stack)))
                stack = []

        if x in DIGITS:
            stack.append(x)
    
    if stack:
        nums.append(int("".join(stack)))
        stack = []

    return nums



def meet_criteria(a, b):

    m = len(a)
    n = len(b)

    length = min(m, n)

    for i in range(length):
        if a[i] < b[i]:
            return True
        if a[i] > b[i]:
            return False

    return True if m <= n else False



correct_order = []

n = len(pairs)
pair_num = 0
for i in range(0, n, 2):
    pair_num += 1
    a = unpack(pairs[i])
    b = unpack(pairs[i+1])
    if meet_criteria(a, b):
        correct_order.append(pair_num)

print(correct_order)















