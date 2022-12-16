class GridHolder:
    def __init__(self, sensors, beacons, target) -> None:

        self.sensors = sensors
        self.beacons = beacons

        self.target = target
        self.coated = set([])
        # we'll need to remove sensors & beacons from this set at the end

    def manhattan_dist(self, one, two):

        (a, b) = one
        (x, y) = two
        return abs(a - x) + abs(b - y)

    def solve(self):

        self.process_all()
        self.remove_appearances(self.sensors)
        self.remove_appearances(self.beacons)

        return len(self.coated)

    def t_movement(self, sensor, beacon):

        points = self.manhattan_dist(sensor, beacon)

        (x, y) = sensor
        points -= abs(y - self.target)

        # we can spend {points} units moving left/right for this pair
        for j in range(x, x+points+1):
            self.coated.add(j)

        for j in range(x, x-(points+1), -1):
            self.coated.add(j)

    def process_all(self):

        n = len(self.sensors)
        for i in range(n):
            sensor = self.sensors[i]
            beacon = self.beacons[i]
            self.t_movement(sensor, beacon)

    def remove_appearances(self, arr):

        for (x, y) in arr:
            if y == self.target:
                if x in self.coated:
                    self.coated.remove(x)
