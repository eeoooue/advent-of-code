
from filereader import FileReader
from inputparser import InputParser
from gridholder_part2_v2 import GridHolder

def solve_part2():

    lines = [line for line in FileReader.get_lines(15, "input.txt") if len(line) > 1]

    sensors = []
    beacons = []
    for line in lines:
        [a, b] = InputParser.get_sensor_position(line)
        [x, y] = InputParser.get_beacon_position(line)
        sensors.append([a, b])
        beacons.append([x, y])

    holder = GridHolder(0)

    prev = 0
    for hundreds in range(40001):
        new_end = hundreds * 100
        print(f"checking from {new_end}..")

        for line in range(prev, new_end):
            holder.target = line
            holder.clear_delta()
            if holder.solve(sensors, beacons):
                print(f"line found, y={line}")
                return

        prev = new_end


solve_part2()

