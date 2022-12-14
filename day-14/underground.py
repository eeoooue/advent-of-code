


class Underground:

    def __init__(self, lines) -> None:
        
        self.m = self.find_floor(lines)
        self.n = 2000
        self.grid = [["." for j in range(self.n)] for i in range(self.m)]

        self.build_paths(lines)

    def find_floor(self, lines):

        lowest = 0
        for line in lines:
            coord_pairs = self.unpack_coords(line)
            for (i, j) in coord_pairs:
                lowest = max(lowest, i)

        return lowest + 1

    def unpack_coords(self, line):

        pairs = []
        for x in line.split(" -> "):
            p = x.split(",")
            pairs.append((int(p[1]), int(p[0])))

        return pairs

    def get_impulse(self, start, end):

        (i, j) = start
        (a, b) = end
        if i != a:
            return (1, 0) if a > i else (-1, 0)
        if j != b:
            return (0, 1) if b > j else (0, -1)

    def add_path(self, start, end):

        (y, x) = self.get_impulse(start, end)
        #print(f"path from {start} to {end} has impulse [{y}, {x}]")

        (i, j) = start
        #print(f"trying to place at [{i}][{j}]")
        self.grid[i][j] = "#"
        while (i, j) != end:
            i += y
            j += x
            #print(f"trying to place at [{i}][{j}]")
            self.grid[i][j] = "#"

    def read_path(self, line):

        coord_pairs = self.unpack_coords(line)
        n = len(coord_pairs)

        for i in range(0, n-1):
            start_pt = coord_pairs[i]
            end_pt = coord_pairs[i+1]
            self.add_path(start_pt, end_pt)

    def build_paths(self, array):

        for line in array:
            self.read_path(line)

        print(f"paths built")