
from filereader import FileReader
from inputparser import InputParser
from gridholder_part2_v2 import GridHolder

lines = [line for line in FileReader.get_lines(15, "input.txt") if len(line) > 1]

sensors = []
beacons = []
for line in lines:
    [a, b] = InputParser.get_sensor_position(line)
    [x, y] = InputParser.get_beacon_position(line)
    sensors.append([a, b])
    beacons.append([x, y])

delta = [0] * 4_000_001


def clear_delta():

    for i in range(4_000_001):
        delta[i] = 0

def t_movement_delta(sensor, beacon, target):

    (a, b) = beacon
    (x, y) = sensor

    points = abs(a - x) + abs(b - y) - abs(y - target)
    
    if points < 0:
        return

    #left_limit
    delta[max(0, x-points)] += 1

    #right limit + 1
    if x + points < 4_000_000:
        delta[x + points + 1] -= 1

def gap_in_delta():

    current = 0
    for x in delta:
        current += x
        if current < 1:
            return True

    return False

def solve(sensors, beacons, target):

    n = len(sensors)
    for i in range(n):
        t_movement_delta(sensors[i], beacons[i], target)
        
    return gap_in_delta()





def solve_part2():

    prev = 0
    for hundreds in range(40001):
        new_end = hundreds * 100
        print(f"checking from {new_end}..")

        for line in range(prev, new_end):
            clear_delta()
            if solve(sensors, beacons, line):
                print(f"line found, y={line}")
                return

        prev = new_end


solve_part2()

