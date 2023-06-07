class FileReader:
    @staticmethod
    def get_lines(filename):

        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


class Interval:
    def __init__(self, i, j) -> None:

        self.start = i
        self.end = j

    def contains(self, other):

        if self.start <= other.start:
            if self.end >= other.end:
                return True

    def overlaps(self, other):

        if self.start <= other.start:
            if self.end >= other.start:
                return True


class Solution:
    def __init__(self, lines) -> None:

        self.lines = lines

    def interpret_range(self, line):

        i = line.index("-")
        start = int(line[:i])
        end = int(line[i + 1 :])

        return Interval(start, end)

    def unpack_intervals(self, line):

        result = []
        for range in line.split(","):
            interval = self.interpret_range(range)
            result.append(interval)

        return result

    def count_containments(self):

        count = 0
        for line in self.lines:
            (a, b) = self.unpack_intervals(line)
            if a.contains(b) or b.contains(a):
                count += 1

        return count

    def count_overlaps(self):

        count = 0
        for line in self.lines:
            (a, b) = self.unpack_intervals(line)
            if a.overlaps(b) or b.overlaps(a):
                count += 1

        return count


lines = FileReader.get_lines("input.txt")
solver = Solution(lines)

ans_part_1 = solver.count_containments()
ans_part_2 = solver.count_overlaps()

print(f"There are {ans_part_1} ranges which fully contain their pair.")
print(f"There are {ans_part_2} assignments in which the ranges overlap.")
