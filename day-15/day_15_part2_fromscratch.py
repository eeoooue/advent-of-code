
from filereader import FileReader
from inputparser import InputParser
from beaconchecker import BeaconChecker

def solve_part2(filename, limit):

    lines = [line for line in FileReader.get_lines(15, filename) if len(line) > 1]

    sensors = []
    beacons = []
    for line in lines:
        [a, b] = InputParser.get_sensor_position(line)
        [x, y] = InputParser.get_beacon_position(line)
        sensors.append([a, b])
        beacons.append([x, y])

    checker = BeaconChecker(sensors, beacons)

    for y in range(limit):
        x = 0
        while x < limit:
            x = checker.next_overlap(x, y)

    (x, y) = checker.solution
    return (x * 4000000) + y

# takes ~1-2 mins for me
ans = solve_part2("input.txt", 4_000_001)

print(f"part 2: the tuning frequency is {ans} Hz (12691026767556 for me)")

