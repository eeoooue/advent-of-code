class InputParser:
    @staticmethod
    def get_sensor_position(line):

        line = InputParser.__crop_by_endpoint(line, ":")
        line = InputParser.__remove_prefix(line, "Sensor at ")
        (x, y) = InputParser.__unpack_x_y(line)

        # print(f"sensor @ ({x}, {y})")
        return (x, y)

    @staticmethod
    def get_beacon_position(line):

        line = InputParser.__crop_by_startpoint(line, ":")
        line = InputParser.__remove_prefix(line, ": closest beacon is at ")
        (x, y) = InputParser.__unpack_x_y(line)

        # print(f"beacon @ ({x}, {y})")
        return (x, y)

    def __crop_by_startpoint(line, startpoint):

        i = line.index(startpoint)
        return line[i:]

    def __crop_by_endpoint(line, endpoint):

        i = line.index(endpoint)
        return line[:i]

    def __remove_prefix(line, prefix):

        i = len(prefix)
        return line[i:].strip()

    def __unpack_x_y(line):

        arr = [x.strip() for x in line.split(",")]
        arr = [int(x[2:]) for x in arr]
        x = int(arr[0])
        y = int(arr[1])

        return (x, y)
