import heapq


class FileReader:
    @staticmethod
    def get_lines(filename):

        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


class Solution:
    def __init__(self, item_list):

        self.elves = []
        self.read_list(item_list)

    def read_list(self, item_list):

        calories = 0
        for item_value in item_list:
            if item_value == "":
                self.add_elf(calories)
                calories = 0
            else:
                calories += int(item_value)
        self.add_elf(calories)

    def add_elf(self, calories):

        if calories > 0:
            self.heap_push(calories)

    def heap_pop(self):

        calories = -heapq.heappop(self.elves)
        return calories

    def heap_push(self, calories):

        heapq.heappush(self.elves, -calories)

    def get_n_largest_values(self, n):

        values = []
        for i in range(n):
            calories = self.heap_pop()
            values.append(calories)

        for calories in values:
            self.heap_push(calories)

        return values

    def sum_largest_elves(self, n):

        values = self.get_n_largest_values(n)
        return sum(values)


item_list = FileReader.get_lines("input.txt")

solver = Solution(item_list)

ans_part_1 = solver.sum_largest_elves(1)
ans_part_2 = solver.sum_largest_elves(3)

print(f"The most calories carried by any elf is {ans_part_1} calories.")
print(f"The top three elves are carrying a total of {ans_part_2} calories.")
