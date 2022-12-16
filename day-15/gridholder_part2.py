class GridHolder:
    def __init__(self, sensors, beacons, target) -> None:

        self.sensors = sensors
        self.beacons = beacons

        self.target = target
        self.coated = [False] * 4_000_001

        # delta traversal ???

        # we'll need to remove sensors & beacons from this set at the end

    def manhattan_dist(self, one, two):

        (a, b) = one
        (x, y) = two
        return abs(a - x) + abs(b - y)

    def solve(self):

        self.process_all()
        #print(f"{len(self.coated)} positions cannot contain a beacon")

        return sum(self.coated)

    def t_movement(self, sensor, beacon):

        points = self.manhattan_dist(sensor, beacon)

        (x, y) = sensor
        points -= abs(y - self.target)

        # we can spend {points} units moving left/right for this pair

        left_start = max(0, x)
        left_limit = min(x+points, 4_000_000)

        for j in range(left_start, left_limit+1):
            self.coated[j] = True

        right_start = min(x, 4_000_000)
        right_limit = max(0, x-points)
        for j in range(right_start, right_limit-1, -1):
            self.coated[j] = True

    def process_all(self):

        n = len(self.sensors)
        for i in range(n):
            sensor = self.sensors[i]
            beacon = self.beacons[i]
            self.t_movement(sensor, beacon)
