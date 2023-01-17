
from gridviewer import GridViewer

class SandSimulation:

    def __init__(self, grid) -> None:
        
        self.grid = grid
        self.source = (0, 500)
        self.m = len(self.grid)
        self.n = len(self.grid[0])

        self.current = None

        self.ongoing = True

        print(f"simulation initialized..")
        self.show_grid()

        for i in range(1000000):
            self.simulate()
            print(f"simulated {i+1} units of sand")

            if not self.ongoing:
                self.show_grid()
                print()
                print(f"only {i} grains could fit")
                break

    def show_grid(self):

        GridViewer.show_grid(self.grid)

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

        if 0 <= i < self.m:
            return True
        return False

    def valid_j(self, j):

        if 0 <= j <= self.n:
            return True

        print(f"I can't have j == [{j}]")
        print(f"VERY BAD NEWS")
        return False

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

        (i, j) = self.current
        i += y
        j += x
        self.current = [i, j]

        if j == self.m:
            self.ongoing = False
    

    def sand_fall(self):

        if not self.ongoing:
            return

        if self.can_move_direction(1, 0):
            self.move_sand(1, 0)
            return self.sand_fall()

        if self.can_move_direction(1, -1):
            self.move_sand(1, -1)
            return self.sand_fall()

        if self.can_move_direction(1, 1):
            self.move_sand(1, 1)
            return self.sand_fall()
        