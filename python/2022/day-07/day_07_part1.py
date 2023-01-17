
class DirNode:

    def __init__(self, x) -> None:

        self.label = x
        self.size = 0
        self.children = set([])

def get_lines():

    import os

    os.chdir("D:\\GitHub\\advent-of-code\\day-07")

    rounds = []
    with open("input.txt", "r") as file:
        for line in file:
            rounds.append(line[:-1])

    return rounds

lines = get_lines()

print(lines)


class Navigation:

    def __init__(self):

        self.nodes = {}
        self.nodes["/"] = DirNode("/")
        self.address = ["/"]

        self.system_space = 70000000
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

    def dir_change_root(self):

        self.address = ["/"]

    def change_directory(self, path):

        if path == "/":
            self.dir_change_root()
            return
        if path == "..":
            self.directory_out()
            return

        self.address.append(path)

    def current_node(self):

        curpath = self.current_path()
        return self.nodes[curpath]

    def add_filesize(self, filesize):

        node = self.current_node()
        node.size += filesize

    def add_directory(self, dirname):

        node = self.current_node()
        childpath = f"{self.current_path()}/{dirname}"

        node.children.add(childpath)
        self.nodes[childpath] = DirNode(childpath)

    def process_line_info(self, line):

        arr = line.split(" ")
        if arr[0] == "dir":
            self.add_directory(arr[1])
        else:
            self.add_filesize(int(arr[0]))

    def all_path_labels(self):

        labels = []

        def explore(node):

            labels.append(node.label)
            for child in node.children:
                explore(self.nodes[child])

        explore(self.nodes["/"])
        return labels


    def get_dir_size(self, label):

        node = self.nodes[label]
        self.size_finding = 0

        def exploresize(node):

            self.size_finding += node.size

            for child in node.children:
                exploresize(self.nodes[child])

        exploresize(node)

        # print(f"size of node[{label}] == {self.size_finding}")

        return self.size_finding

    def space_remaining(self):

        self.dir_change_root()
        rootsize = self.get_dir_size("/")
        self.system_using = rootsize

        print(f"root dir size is {rootsize}")

        return self.system_space - self.system_using





nav = Navigation()

for line in lines:
    if line[:4] == "$ cd":
        directory = line[5:]
        nav.change_directory(directory)

    if line[0] != "$":
        nav.process_line_info(line)


dirsizes = []

ans = 0
labels = nav.all_path_labels()
for label in labels:
    directory_total = nav.get_dir_size(label)

    dirsizes.append(directory_total)

    if directory_total <= 100000:
        ans += directory_total


print(f"the answer to part 1 might be : {ans}")


space_remaining = nav.space_remaining()

space_needed = 30000000

min_deletion_size = max(0, 30000000 - space_remaining)

print(f"find dir of size >= {min_deletion_size}")


dirsizes.sort(reverse=True)

while dirsizes:
    x = dirsizes.pop()
    if x >= min_deletion_size:
        print(f"can delete a dir of size {x}")
        break