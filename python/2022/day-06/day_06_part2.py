

def get_lines():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-06")

    rounds = []
    with open("input.txt", "r") as file:
        for line in file:
            return line[:-1]

line = get_lines()

def all_unique(table):

    count = 0
    members = set([])
    for x in table:
        if table[x]:
            count += table[x]
            members.add(x)

    if len(members) == count:
        return True
    return False



def first_distinct(s, count):

    n = len(s)

    ABC = "abcdefghijklmnopqrstuvwxyz"
    table = {x: 0 for x in ABC}

    for i in range(count):
        x = s[i]
        table[x] += 1
    if all_unique(table):
        return s[:count]

    for i in range(n-count):
        a = s[i]
        b = s[i+count]
        table[a] -= 1
        table[b] += 1
        if all_unique(table):
            print(f"{i+count+1} chars checked")
            return s[i+1:i+count+1]

key = first_distinct(line, 14)

print(f"starter code = {key}")