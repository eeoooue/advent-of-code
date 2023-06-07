# advent-of-code/2022/day03
class FileReader:
    @staticmethod
    def get_lines(filename):
        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


class Solution:
    def __init__(self, lines) -> None:
        self.lines = lines
        self.points = {}
        self.build_scoring_system()

    def build_scoring_system(self):
        ABC = "_abcdefghijklmnopqrstuvwxyz"
        for i, x in enumerate(ABC):
            self.points[x] = i
            self.points[x.upper()] = i + 26

    def split_halfway(self, s):
        i = len(s) // 2
        a = s[:i]
        b = s[i:]

        return [a, b]

    def get_intersection(self, shared, rucksack):
        intersection = set([])
        for item in rucksack:
            if item in shared:
                intersection.add(item)

        return intersection

    def find_common_element(self, group):
        shared = set(group[0])
        for rucksack in group:
            shared = self.get_intersection(shared, rucksack)

        for item in shared:
            return item

    def sum_rucksack_priorities(self):
        total = 0
        for line in self.lines:
            compartments = self.split_halfway(line)
            item = self.find_common_element(compartments)
            total += self.points[item]

        return total

    def sum_badge_values(self):
        n = len(self.lines)

        total = 0
        for i in range(0, n - 2, 3):
            group = self.lines[i : i + 3]
            badge = self.find_common_element(group)
            total += self.points[badge]

        return total


lines = FileReader.get_lines("input.txt")
solver = Solution(lines)

ans_part_1 = solver.sum_rucksack_priorities()
ans_part_2 = solver.sum_badge_values()

print(f"The sum of common item priorities is {ans_part_1}.")
print(f"The sum of group badge priorities is {ans_part_2}.")
