

def get_lines():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-05")

    rounds = []
    with open("input.txt", "r") as file:
        for line in file:
            rounds.append(line[:-1])

    return rounds

class StackSystem:

    def __init__(self):
        
        self.stacks = {i+1: [] for i in range(9)}

    def start_stack(self, i, arr):
        
        for x in arr:
            self.push(i, x)

    def push(self, i, x):

        self.stacks[i].append(x)
    
    def pop(self, i):

        return self.stacks[i].pop()

    def move(self, a, b):

        x = self.pop(a)
        self.push(b, x)

    def read_command(self, command):

        line = command.split(" ")

        move_count = int(line[1])
        a = int(line[3])
        b = int(line[5])

        for i in range(move_count):
            self.move(a, b)

    def cream_top(self):

        build = ""
        for i in range(9):
            if self.stacks[i+1]:
                build += self.stacks[i+1][-1]
        
        return build



lines = get_lines()



system = StackSystem()

system.start_stack(1, "WRF")

system.start_stack(2, "THMCDVWP")

system.start_stack(3, "PMZNL")

system.start_stack(4, "JCHR")

system.start_stack(5, "CPGHQTB")

system.start_stack(6, "GCWLFZ")

system.start_stack(7, "WVLQZJGC")

system.start_stack(8, "PNRFWTVC")

system.start_stack(9, "JWHGRSV")


for line in lines:
    system.read_command(line)
    print(line)



ans = system.cream_top()
print(ans)