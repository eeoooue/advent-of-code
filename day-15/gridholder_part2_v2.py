class GridHolder:
    def __init__(self, target) -> None:

        self.target = target
        self.delta = [0] * 4_000_001

    def clear_delta(self):

        for i in range(4_000_001):
            self.delta[i] = 0

    def gap_in_delta(self):

        current = 0
        for x in self.delta:
            current += x
            if current < 1:
                return True

        return False

    def solve(self, sensors, beacons):

        n = len(sensors)
        for i in range(n):
            self.t_movement_delta(sensors[i], beacons[i])
        
        return self.gap_in_delta()

    def t_movement_delta(self, sensor, beacon):

        (a, b) = beacon
        (x, y) = sensor

        points = abs(a - x) + abs(b - y) - abs(y - self.target)
        
        if points < 0:
            return

        #left_limit
        self.delta[max(0, x-points)] += 1

        #right limit + 1
        if x + points < 4_000_000:
            self.delta[x + points + 1] -= 1