class FileReader:
    @staticmethod
    def get_lines(filename):

        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


class InputParser:
    def __init__(self, lines) -> None:

        self.supplies = []
        self.commands = []
        self.config = []
        self.process_input(lines)

    def process_input(self, lines):

        for line in lines:
            if line[:4] == "move":
                self.commands.append(line)
            elif len(line) > 2:
                self.add_supplies(line)

        self.build_config()

    def add_supplies(self, line):

        layer = []
        for i in range(1, len(line), 4):
            layer.append(line[i])

        if layer:
            self.supplies.append(layer)

    def build_config(self):

        n = len(self.supplies[0])
        for i in range(n):
            layer = self.get_layer(i)
            self.config.append(layer)

    def get_layer(self, j):

        m = len(self.supplies)
        k = int(self.supplies[-1][j])

        build = ""
        for i in range(m - 2, -1, -1):
            if self.supplies[i][j] != " ":
                build += self.supplies[i][j]

        return (k, build)


class SupplyStacks:
    def __init__(self, config) -> None:

        self.stacks = {}
        for (k, arr) in config:
            self.stacks[k] = list(arr)

    def push_item(self, i, x):

        self.stacks[i].append(x)

    def pop_item(self, i):

        return self.stacks[i].pop()

    def cream_top(self):

        build = ""
        for k in self.stacks:
            if self.stacks[k]:
                build += self.stacks[k][-1]

        return build


class Command:
    def __init__(self, origin, destination, crates) -> None:

        self.origin = origin
        self.destination = destination
        self.crates = crates


class CrateMover:
    def __init__(self, supplies: SupplyStacks, model_number) -> None:

        self.supplies = supplies
        self.model = model_number
        self.holding = []

    def load_from(self, i):

        item = self.supplies.pop_item(i)
        self.holding.append(item)

    def unload_to(self, i):

        item = self.holding.pop()
        self.supplies.push_item(i, item)

    def move_crates(self, origin, destination, count):

        for i in range(count):
            self.load_from(origin)

        while self.holding:
            self.unload_to(destination)

    def operate(self, command: Command):

        match self.model:
            case 9000:
                for i in range(command.crates):
                    self.move_crates(command.origin, command.destination, 1)
            case 9001:
                self.move_crates(command.origin, command.destination, command.crates)


class Solution:
    def __init__(self, config, lines):

        self.config = config
        self.lines = lines

    def interpret_command(self, line):

        command = line.split(" ")
        crates_to_move = int(command[1])
        origin = int(command[3])
        destination = int(command[5])

        return Command(origin, destination, crates_to_move)

    def rearrange_supplies(self, crane_model):

        supplies = SupplyStacks(self.config)
        crane = CrateMover(supplies, crane_model)

        for line in self.lines:
            command = self.interpret_command(line)
            crane.operate(command)

        return supplies.cream_top()


lines = FileReader.get_lines("input.txt")
parser = InputParser(lines)
solver = Solution(parser.config, parser.commands)

ans_part_1 = solver.rearrange_supplies(9000)
ans_part_2 = solver.rearrange_supplies(9001)

print(f"The crates would read '{ans_part_1}' after being rearranged.")
print(f"Using the CrateMover 9001, the crates would spell '{ans_part_2}' instead.")
