
from filereader import FileReader
from underground import Underground

from sandsimulation import SandSimulation

lines = [line for line in FileReader.get_lines(14, "input.txt") if len(line) > 1]

# sand always pours in from 500,0 ?

underground = Underground(lines)

simulation = SandSimulation(underground.grid)



