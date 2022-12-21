

import collections

class MonkeyNode:

    def __init__(self, name, string) -> None:
        
        self.name = name
        self.string = string

        self.value = 0
        self.found = False

        self.operator = None
        self.one = None
        self.two = None

        self.process_info()

    def process_info(self):

        if self.contains_space(self.string):
            self.unpack()
        else:
            self.assign_value(int(self.string))

    def contains_space(self, string):

        for x in string:
            if x == " ":
                return True
        return False

    def assign_value(self, x):

        self.found = True
        self.value = x

    def unpack(self):

        arr = self.string.split(" ")

        self.one = arr[0]
        self.operator = arr[1]
        self.two = arr[2]

    


class MonkeyPen:

    def __init__(self) -> None:
    
        self.nodes = {}
        self.values = {}

    def get_monkey_value(self, name):

        return self.values[name]

    def solve_all(self):

        unsolved = set([name for name in self.nodes])
        while unsolved:

            queue = [x for x in unsolved]
            while queue:
                name = queue.pop()
                if self.solve_node(name):
                    unsolved.remove(name)

    def evaluate_operation(self, a, operator, b):

        if operator == "+":
            return a + b

        if operator == "-":
            return a - b

        if operator == "*":
            return a * b

        if operator == "/":
            return a / b
    

    def solve_node(self, name):

        node = self.nodes[name]

        if node.found:
            self.values[name] = node.value
            return True

        if node.one in self.values:
            if node.two in self.values:
                a = self.values[node.one]
                b = self.values[node.two]
                x = self.evaluate_operation(a, node.operator, b)
                node.assign_value(x)
                return self.solve_node(name)

        return False






    def interpret_array(self, arr):

        for line in arr:
            self.interpret_line(line)

    def interpret_line(self, line):

        node = self.string_to_monkey_node(line)
        self.nodes[node.name] = node

    def string_to_monkey_node(self, line):

        i = line.index(":")
        return MonkeyNode(line[:i], line[i+2:])
        








