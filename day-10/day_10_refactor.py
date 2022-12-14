
def get_lines():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-10")

    rounds = []
    with open("input.txt", "r") as file:
        for line in file:
            rounds.append(line[:-1])

    return rounds

class Simulation:

    def __init__(self) -> None:
        
        self.cycles = []
        self.t = 0
        self.value = 1
        self.drawing = ["." for i in range(240)]
        self.active = [0 for i in range(240)]

    def print_screen(self):

        for i in range(6):
            line = []
            for j in range(40):
                line.append(self.drawing[(i*40)+j])
            print("".join(line))

    def update_sprite(self):

        self.active = [0 for i in range(240)]

        x_pos = self.value
        a = (x_pos - 1) % 40
        b = (x_pos) % 40
        c = (x_pos + 1) % 40

        for i in range(6):
            self.active[(i*40)+a] = 1
            self.active[(i*40)+b] = 1
            self.active[(i*40)+c] = 1

    def cycle(self):
        
        self.cycles.append(self.value)
        self.update_sprite()
        self.t += 1

        if self.active[self.t-1] == 1:
            self.drawing[self.t-1] = "#"

    def spend_cycles(self, n):

        for i in range(n):
            self.cycle()
    
    def interpret_line(self, line):

        if line[0] == "n":
            self.spend_cycles(1)
        
        if line[0] == "a":
            #print(f"will increment value by {line[5:]}")
            self.spend_cycles(2)
            self.value += int(line[5:])

        print(line)
        self.print_screen()
        print("...")

    def serve_query(self, arr):

        response = []
        for i in arr:
            response.append(i * self.cycles[i-1])
        return response


mysim = Simulation()


lines = get_lines()
for line in lines:
    mysim.interpret_line(line)

#print(mysim.cycles)

query_arr = [20, 60, 100, 140, 180, 220]
response = mysim.serve_query(query_arr)

print(f"returns {response} ;; sum = {sum(response)}")








