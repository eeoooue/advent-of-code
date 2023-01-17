
from filereader import FileReader
from underground import Underground

from sandsimulation2 import SandSimulation2

lines = [line for line in FileReader.get_lines(14, "input.txt") if len(line) > 1]

# sand always pours in from 500,0 ?

underground = Underground(lines)

simulation = SandSimulation2(underground.grid)

ans = simulation.run_simulation()

print(f"{ans} grains came to rest (23416 for me)")


# 23416 is the answer for me



