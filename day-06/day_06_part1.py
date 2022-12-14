

def get_lines():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-06")

    rounds = []
    with open("input.txt", "r") as file:
        for line in file:
            return line[:-1]

line = get_lines()

def four_unique(table):

    members = set([])
    for x in table:
        if table[x]:
            members.add(x)

    if len(members) == 4:
        return True
    return False



def first_four(s):

    n = len(s)

    ABC = "abcdefghijklmnopqrstuvwxyz"
    table = {x: 0 for x in ABC}

    for i in range(4):
        x = s[i]
        table[x] += 1
    if four_unique(table):
        return s[:4]

    for i in range(n-4):
        a = s[i]
        b = s[i+4]
        table[a] -= 1
        table[b] += 1
        if four_unique(table):
            print(f"{i+5} chars checked")
            return s[i+1:i+5]

key = first_four(line)

print(f"starter code = {key}")