
from filereader import FileReader

lines = FileReader.get_lines(12, "input.txt")

def interpret_grid(lines, part2):

    ALPHALOOK = {x: i for i, x in enumerate("abcdefghijklmnopqrstuvwxyz")}
    ALPHALOOK["S"] = 0
    ALPHALOOK["E"] = 25

    grid = []
    m = len(lines)
    n = len(lines[0])

    options = []
    end = None

    for i in range(m):
        line = []
        for j in range(n):
            line.append(ALPHALOOK[lines[i][j]])
        grid.append(line)

    for i in range(m):
        for j in range(n):
            if lines[i][j] == "S":
                options.append((i, j))
            if lines[i][j] == "E":
                end = (i, j)

    if part2:
        for i in range(m):
            for j in range(n):
                if lines[i][j] == "a":
                    options.append((i, j))

    return (grid, options, end)


def solve(grid, start, end):

    m = len(grid)
    n = len(grid[0])

    from collections import deque

    def can_move(height, i, j):

        if 0 <= i < m:
            if 0 <= j < n:
                if grid[i][j] <= height+1:
                    return True
        return False

    def explore(position, moves):

        (i, j) = position
        if (i, j) in min_moves and min_moves[(i, j)] <= moves:
            return

        min_moves[(i, j)] = moves

        height = grid[i][j]

        W = (i-1, j)
        A = (i, j-1)
        S = (i+1, j)
        D = (i, j+1)

        for (a, b) in (W,A,S,D):
            if can_move(height, a, b):
                queue.append(((a, b), moves+1))

    queue = deque([])
    queue.append((start, 0))
    min_moves = {}

    while queue:
        (position, moves) = queue.popleft()
        explore(position, moves)

    if end not in min_moves:
        #print(f"something went wrong")
        return float("inf")

    return min_moves[end]

(grid, options, end) = interpret_grid(lines, True)

best = float("inf")
for start in options:
    ans = solve(grid, start, end)
    best = min(best, ans)

print(best)

#497 for part 1
#492 for part 2