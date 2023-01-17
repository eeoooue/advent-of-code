
class FileReader:

    @staticmethod
    def get_lines(day, filename):

        path = f"D:\\GitHub\\advent-of-code\\day-{day}"

        lines = []
        with open(f"{path}\\{filename}", "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines
