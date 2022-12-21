
from filereader import FileReader

from monkeynode import MonkeyPen

def get_lines(filename):

    return [line for line in FileReader.get_lines(21, filename)]

lines = get_lines("input.txt")

pen = MonkeyPen()

pen.interpret_array(lines)

pen.solve_all()

part1 = pen.get_monkey_value("root")

print(f"part 1 = {part1} (83056452926300) for me")
