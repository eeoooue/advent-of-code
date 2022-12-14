
import os

class FileReader:

    @staticmethod
    def get_lines(day, filename):

        os.chdir(f"D:\\GitHub\\advent-of-code\\day-{day}")

        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


