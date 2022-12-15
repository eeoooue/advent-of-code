class LogicEngine:
    @staticmethod
    def manhattan_dist(one, two):

        (a, b) = one
        (x, y) = two

        return abs(a - x) + abs(b - y)

    @staticmethod
    def sensor_relevant(x, y, manhat, target):

        if y == target:
            return True

        if y < target:
            if y + manhat >= target:
                return True

        if y > target:
            if y - manhat <= target:
                return True

        print(f"sensor @ ({x}, {y}) can be ignored")
        return False
