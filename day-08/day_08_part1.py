

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

def scrape_left(i, j):

    best = -1
    while j+1 < n:
        j += 1
        best = max(best, tree_grid[i][j])

    return best

def scrape_right(i, j):

    best = -1
    while j-1 >= 0:
        j -= 1
        best = max(best, tree_grid[i][j])

    return best

def scrape_up(i, j):

    best = -1
    while i-1 >= 0:
        i -= 1
        best = max(best, tree_grid[i][j])

    return best

def scrape_down(i, j):

    best = -1
    while i+1 < m:
        i += 1
        best = max(best, tree_grid[i][j])

    return best



def is_visible(i, j):

    height = tree_grid[i][j]

    vals = []
    vals.append(scrape_left(i, j))
    vals.append(scrape_right(i, j))
    vals.append(scrape_up(i, j))
    vals.append(scrape_down(i, j))

    for blocker in vals:
        if height > blocker:
            return True
    return False

count = 0
for i in range(m):
    for j in range(n):
        if is_visible(i, j):
            count += 1

print(f"count of visible trees = {count}")




