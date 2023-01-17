
from gridviewer import GridViewer

class SandSimulation2:

    def __init__(self, grid) -> None:
        
        self.grid = grid
        self.n = len(self.grid[0])

        self.grid.append(["." for j in range(self.n)])
        self.grid.append(["#" for j in range(self.n)])

        self.source = (0, 500)
        self.m = len(self.grid)

        self.current = None
        self.ongoing = True

    def show_grid(self):

        GridViewer.show_grid(self.grid)

    def run_simulation(self):

        grain_count = 0
        while self.ongoing and self.grid[0][500] != "O":
            self.simulate()
            grain_count += 1
        
        return grain_count

    def simulate(self):

        if not self.ongoing:
            return

        (i, j) = self.source
        self.current = [i, j]

        self.sand_fall()

        if self.ongoing:
            (i, j) = self.current
            self.grid[i][j] = "O"

    def valid_i(self, i):

        return 0 <= i < self.m

    def valid_j(self, j):

        return 0 <= j <= self.n

    def can_move_direction(self, y, x):

        (i, j) = self.current
        i += y
        j += x

        if not self.valid_i(i) or not self.valid_j(j):
            self.ongoing = False
            return True
        
        if self.grid[i][j] == ".":
            return True
        return False

    def move_sand(self, y, x):

        self.current[0] += y
        self.current[1] += x

    def sand_fall(self):

        while self.ongoing:

            if self.can_move_direction(1, 0):
                self.move_sand(1, 0)
                continue

            if self.can_move_direction(1, -1):
                self.move_sand(1, -1)
                continue

            if self.can_move_direction(1, 1):
                self.move_sand(1, 1)
                continue

            break
        