
from filereader import FileReader
from inputparser import InputParser
from gridholder_part2_v3 import GridHolder
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

    print(f"no solution found")


def get_tuning(x, y):


    return (x * 4000000) + y


#solve_part2("example.txt", 21)

#solve_part2("input.txt", 4_000_001)



# x=3172756, y=2767556

ans = get_tuning(x=3172756, y=2767556)

print(ans)

