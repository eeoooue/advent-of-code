class GridHolder:
    def __init__(self, sensors, beacons, target) -> None:

        self.sensors = sensors
        self.beacons = beacons

        self.target = target

        self.coated = set([])
        # we'll need to remove sensors & beacons from this set at the end
        self.queue = []
        self.limiter = 0

    def manhattan_dist(self, one, two):

        (a, b) = one
        (x, y) = two

        return abs(a - x) + abs(b - y)

    def solve(self):

        self.process_all()
        self.remove_appearances(self.sensors)
        self.remove_appearances(self.beacons)

        print(f"{len(self.coated)} positions cannot contain a beacon")

    def explore(self, x, y, depth):

        if y == self.target:
            self.coated.add(x)

        if depth == self.limiter:
            return

        self.queue.append((x - 1, y, depth + 1))
        self.queue.append((x + 1, y, depth + 1))
        self.queue.append((x, y - 1, depth + 1))
        self.queue.append((x, y + 1, depth + 1))

    def expand(self, sensor, beacon):

        distance = self.manhattan_dist(sensor, beacon)
        self.limiter = distance

        (x, y) = sensor
        self.queue.append((x, y, 0))

        while self.queue:
            (x, y, d) = self.queue.pop()
            self.explore(x, y, d)

    def t_movement(self, sensor, beacon):

        points = self.manhattan_dist(sensor, beacon)

        (x, y) = sensor
        points -= abs(y - self.target)

        print(f"we can spend {points} units moving left/right for this pair")

        if points < 0:
            return

        for i in range(points + 1):
            self.coated.add(x + i)
            self.coated.add(x - i)

    def process_all(self):

        n = len(self.sensors)

        print(f"attempting to process {n} pairs")

        for i in range(n):
            sensor = self.sensors[i]
            beacon = self.beacons[i]
            # self.expand(sensor, beacon)
            self.t_movement(sensor, beacon)
            print(f"processed ({i+1} / {n}) sensor-beacon pairs")

        print(f"processing complete")

    def remove_appearances(self, arr):

        for (x, y) in arr:
            if y == self.target:
                if x in self.coated:
                    self.coated.remove(x)
