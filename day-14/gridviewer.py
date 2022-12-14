
class GridViewer:

    @staticmethod
    def show_grid(grid):

        m = len(grid)
        n = len(grid[0])

        left_start = GridViewer.__find_left_start(grid, m, n)
        right_end = GridViewer.__find_right_end(grid, m, n)

        for i in range(m):
            line = grid[i]
            visible_segment = line[left_start:right_end+1]
            print("".join(visible_segment))

    def __find_left_start(grid, m, n):

        best = n - 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] != ".":
                    best = min(best, j)
                    break

        return best

    def __find_right_end(grid, m, n):

        best = 0
        for i in range(m):
            for j in range(n-1, -1, -1):
                if grid[i][j] != ".":
                    best = max(best, j)
                    break

        return best

    
        
