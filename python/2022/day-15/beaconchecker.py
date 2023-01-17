
class BeaconChecker:

    def __init__(self, sensors, beacons) -> None:
        
        self.sensors = sensors
        self.beacons = beacons
        self.ranges = []
        self.solution = (-1, -1)
        self.get_ranges()

    def get_ranges(self):

        n = len(self.sensors)
        for i in range(n):
            (a, b) = self.beacons[i]
            (x, y) = self.sensors[i]
            score = self.manhattan_distance(a, b, x, y)
            self.ranges.append(score)

    def manhattan_distance(self, a, b, x, y):

        return abs(a - x) + abs(b - y)

    def escape_sensor(self, x, y, i):

        (a, b) = self.sensors[i]
        points = self.ranges[i] - abs(y - b)
        return a + points + 1
    

    def next_overlap(self, x, y):

        n = len(self.sensors)
        for i in range(n):
            (a, b) = self.sensors[i]
            score = self.manhattan_distance(a, b, x, y)
            if score <= self.ranges[i]:
                return self.escape_sensor(x, y, i)

        self.solution = (x, y)
        return x + 525_300_887_039
