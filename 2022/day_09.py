# advent-of-code/2022/day09
class FileReader:
    @staticmethod
    def get_lines(filename):
        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


class KnotNode:
    def __init__(self):
        self.MOVELOOK = {
            "U": (-1, 0),
            "L": (0, -1),
            "R": (0, 1),
            "D": (1, 0),
        }

        self.position = [0, 0]
        self.next = None
        self.visited = set([])
        self.mark_visited()

    def mark_visited(self):
        (i, j) = self.position
        self.visited.add((i, j))

    def move_me(self, d):
        (i, j) = self.position
        (y, x) = self.MOVELOOK[d]
        self.position = [i + y, j + x]

    def already_touching(self):
        (i, j) = self.following
        for a in range(i - 1, i + 2):
            for b in range(j - 1, j + 2):
                if [a, b] == self.position:
                    return True
        return False

    def chase_row(self, i):
        if self.position[0] < i:
            self.move_me("D")
        else:
            self.move_me("U")

    def chase_column(self, j):
        if self.position[1] < j:
            self.move_me("R")
        else:
            self.move_me("L")

    def diagonal_chase(self):
        (i, j) = self.following
        self.chase_row(i)
        self.chase_column(j)
        self.mark_visited()

    def follow_offset(self, y, x):
        (i, j) = self.position
        if [i + y, j + x] == self.following:
            return True

    def follow_position(self, i, j):
        self.following = [i, j]
        self.drag_me()

        if not self.next:
            self.mark_visited()

    def drag_me(self):
        if self.already_touching():
            return
        for d in self.MOVELOOK:
            (y, x) = self.MOVELOOK[d]
            if self.follow_offset(2 * y, 2 * x):
                return self.move_me(d)

        self.diagonal_chase()


class Rope:
    def __init__(self, length) -> None:
        self.head = self.build_rope(length)

    def build_rope(self, length):
        root = KnotNode()
        node = root
        for i in range(length - 1):
            node.next = KnotNode()
            node = node.next

        return root

    def get_tail(self):
        node = self.head
        while node.next:
            node = node.next

        return node

    def interpret_command(self, line):
        arr = line.split(" ")
        d = arr[0]
        amount = int(arr[1])
        for _ in range(amount):
            self.move_head(d)
            self.update_rope()

    def move_head(self, d):
        self.head.move_me(d)

    def update_rope(self):
        node = self.head

        while node.next:
            (i, j) = node.position
            node = node.next
            node.follow_position(i, j)

    def count_tail_placements(self):
        node = self.get_tail()
        count = len(node.visited)
        return count


def solve(length):
    my_rope = Rope(length)
    lines = FileReader.get_lines("input.txt")
    for line in lines:
        my_rope.interpret_command(line)

    return my_rope.count_tail_placements()


print(f"Part 1: {solve(2)} places visited")
print(f"Part 2: {solve(10)} places visited")
