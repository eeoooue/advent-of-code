

def get_lines():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-08")

    rounds = []
    with open("input.txt", "r") as file:
        for line in file:
            rounds.append(line[:-1])

    return rounds

def tree_matrix(lines):

    m = len(lines)
    n = len(lines[0])

    treegrid = [[int(x) for x in line] for line in lines]

    return treegrid

def visibility_matrix(treegrid):

    m = len(treegrid)
    n = len(treegrid[0])

    matrix = [[0 for j in range(n)] for i in range(m)]

    return matrix

lines = get_lines()

tree_grid = tree_matrix(lines)

visibility = visibility_matrix(tree_grid)

m = len(tree_grid)
n = len(tree_grid[0])

for line in tree_grid:
    print(line)



def look_left(i, j):

    height = tree_grid[i][j]
    score = 0
    while j + 1 < n:
        j += 1
        score += 1
        if tree_grid[i][j] >= height:
            break

    return score




def look_right(i, j):

    height = tree_grid[i][j]
    score = 0
    while j - 1 >= 0:
        j -= 1
        score += 1
        if tree_grid[i][j] >= height:
            break

    return score


def look_up(i, j):

    height = tree_grid[i][j]
    score = 0
    while i - 1 >= 0:
        i -= 1
        score += 1
        if tree_grid[i][j] >= height:
            break

    return score


def look_down(i, j):

    height = tree_grid[i][j]
    score = 0
    while i + 1 < m:
        i += 1
        score += 1
        if tree_grid[i][j] >= height:
            break

    return score


def get_score(i, j):

    score = 1
    score *= look_left(i, j)
    score *= look_right(i, j)
    score *= look_up(i, j)
    score *= look_down(i, j)

    return score

best = 0
for i in range(m):
    for j in range(n):
        score = get_score(i, j)
        best = max(best, score)

print(f"best tree score = {best}")




