# advent-of-code/2022/day06
class FileReader:
    @staticmethod
    def get_lines(filename):
        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


class Solution:
    def __init__(self, datastream, marker_length) -> None:
        self.stream = datastream
        self.m = marker_length
        self.n = len(datastream)

        self.table = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}
        self.active = set([])
        self.chars_read = 0

    def initialize_window(self):
        for i in range(self.m):
            self.read_character(self.stream[i])

    def slide_window(self, i):
        self.drop_character(self.stream[i])
        self.read_character(self.stream[i + self.m])

    def marker_complete(self):
        return len(self.active) == self.m

    def drop_character(self, x):
        self.table[x] -= 1
        if self.table[x] == 0:
            self.active.remove(x)

    def read_character(self, x):
        if self.table[x] == 0:
            self.active.add(x)
        self.table[x] += 1
        self.chars_read += 1

    def solve(self):
        self.initialize_window()
        if self.marker_complete():
            return self.chars_read

        for i in range(self.n - self.m):
            self.slide_window(i)
            if self.marker_complete():
                return self.chars_read


lines = FileReader.get_lines("input.txt")

solver = Solution(lines[0], 4)
ans_part_1 = solver.solve()

solver = Solution(lines[0], 14)
ans_part_2 = solver.solve()

print(f"First start-of-packet marker found after {ans_part_1} characters.")
print(f"First start-of-message marker found after {ans_part_2} characters.")
