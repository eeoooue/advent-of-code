
from filereader import FileReader
from inputparser import InputParser
from gridholder import GridHolder
from logicengine import LogicEngine



def solve_part1(filename, target_line):

    lines = [line for line in FileReader.get_lines(15, filename) if len(line) > 1]

    sensors = []
    beacons = []
    for line in lines:
        [a, b] = InputParser.get_sensor_position(line)
        [x, y] = InputParser.get_beacon_position(line)
        
        manhattan_dist = LogicEngine.manhattan_dist((a, b), (x, y))
        if LogicEngine.sensor_relevant(a, b, manhattan_dist, target_line):
            sensors.append([a, b])
            beacons.append([x, y])

    holder = GridHolder(sensors, beacons, target_line)
    holder.solve()

    return



#solve_part1("example.txt", 10)


# part 1 = 4883971 for me
solve_part1("input.txt", 2000000)

