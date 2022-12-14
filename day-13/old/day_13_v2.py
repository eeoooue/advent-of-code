
from filereader import FileReader

pairs = [line for line in FileReader.get_lines(13, "example.txt") if len(line) > 1]

print(pairs)

DIGITS = set("0123456789")


def unpack(s):


    def clear_stack():

        if stack:
            x = "".join(stack)
            nums.append(int(x))

        while stack:
            stack.pop()

    nums = []

    
    n = len(s)

    stack = []

    i = 1
    while i < n:

        if s[i] in DIGITS:
            stack.append(s[i])
        else:
            clear_stack()

        if s[i] == "[":
            stopper = i
            table = {"[": 0, "]": 0}
            for j in range(i, n):
                x = s[j]
                if x in table:
                    table[x] += 1
                if table["["] == table["]"]:
                    stopper = j
                    break
            
            nums.append(unpack(s[i:stopper+1]))
            i = stopper

        i += 1

    
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

    print(f"{pairs[i]} unpacks to {a}")
    print(f"{pairs[i+1]} unpacks to {b}")

print(correct_order)















