# advent-of-code/2022/day07
class FileReader:
    @staticmethod
    def get_lines(filename):

        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


class DirectoryNode:
    def __init__(self, x) -> None:

        self.label = x
        self.size = 0
        self.children = set([])


class FileSystem:
    def __init__(self):

        self.nodes = {}
        self.nodes["/"] = DirectoryNode("/")
        self.address = ["/"]

        self.system_space = 70_000_000
        self.system_using = 0

    def current_path(self):

        build = ""
        for x in self.address:
            build += f"{x}/"
        return build[:-1]

    def directory_out(self):

        if self.address:
            self.address.pop()
        if not self.address:
            self.address = ["/"]

    def change_directory(self, path):

        if path == "/":
            self.address = ["/"]
            return
        if path == "..":
            self.directory_out()
            return

        self.address.append(path)

    def get_current_node(self):

        curpath = self.current_path()
        return self.nodes[curpath]

    def add_filesize(self, filesize):

        node = self.get_current_node()
        node.size += filesize

    def add_directory(self, dirname):

        node = self.get_current_node()
        childpath = f"{self.current_path()}/{dirname}"

        node.children.add(childpath)
        self.nodes[childpath] = DirectoryNode(childpath)

    def process_line_info(self, line):

        arr = line.split(" ")
        if arr[0] == "dir":
            self.add_directory(arr[1])
        else:
            self.add_filesize(int(arr[0]))

    def get_directory_size(self, label):

        node = self.nodes[label]
        self.size_finding = 0

        def exploresize(node):

            self.size_finding += node.size
            for child in node.children:
                exploresize(self.nodes[child])

        exploresize(node)

        return self.size_finding

    def space_remaining(self):

        self.address = ["/"]
        rootsize = self.get_directory_size("/")
        self.system_using = rootsize

        return self.system_space - self.system_using
    

class Solution:
    def __init__(self, lines) -> None:
        
        self.filesys = FileSystem()
        self.interpret_filesystem(lines)
        self.get_dirsizes()

    def interpret_filesystem(self, lines):

        for line in lines:
            if line[:4] == "$ cd":
                directory = line[5:]
                self.filesys.change_directory(directory)

            if line[0] != "$":
                self.filesys.process_line_info(line)

    def get_dirsizes(self):
        
        self.dirsizes = []

        for label in self.filesys.nodes:
            directory_total = self.filesys.get_directory_size(label)
            self.dirsizes.append(directory_total)

        self.dirsizes.sort()

    def solvept1(self):

        ans = 0
        for x in self.dirsizes:
            if x > 100000:
                break
            ans += x

        return ans

    def solvept2(self):

        space_remaining = self.filesys.space_remaining()
        space_needed = 30000000
        min_deletion_size = max(0, space_needed - space_remaining)
        
        for x in self.dirsizes:
            if x >= min_deletion_size:
                return x

lines = FileReader.get_lines("input.txt")
solver = Solution(lines)

print(f"The sum of the total sizes of the directories meeting the criteria is {solver.solvept1()}")
print(f"The smallest directory that could be deleted for the update is of size {solver.solvept2()}")