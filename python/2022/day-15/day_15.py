
from filereader import FileReader
from inputparser import InputParser
from gridholder import GridHolder
from beaconchecker import BeaconChecker


# check just outside range of each sensor ?

def load_all(filename):

    for line in FileReader.get_lines(15, filename):
        if len(line) > 1:
            [a, b] = InputParser.get_sensor_position(line)
            [x, y] = InputParser.get_beacon_position(line)
            sensors.append([a, b])
            beacons.append([x, y])

def solve_part1(filename, target_line):

    if not sensors:
        load_all(filename)

    holder = GridHolder(sensors, beacons, target_line)
    return holder.solve()

def solve_part2(filename, limit):

    if not sensors:
        load_all(filename)

    checker = BeaconChecker(sensors, beacons)
    for y in range(limit):
        x = 0
        while x < limit:
            x = checker.next_overlap(x, y)

    (x, y) = checker.solution
    return (x * 4000000) + y

sensors = []
beacons = []

ans_1 = solve_part1("input.txt", 2000000)
print(f"part 1: {ans_1} positions cannot contain a beacon (4883971 for me)")

#takes ~1-2 mins for me
ans_2 = solve_part2("input.txt", 4_000_001)
print(f"part 2: the tuning frequency is {ans_2} Hz (12691026767556 for me)")
