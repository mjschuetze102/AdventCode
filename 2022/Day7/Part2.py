class Node:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.children = {}
        self.size = 0

    def get_size(self):
        size = self.size

        for child in self.children.values():
            size += child.get_size()

        return size

    def get_children(self):
        nodes = list(self.children.values()) if len(self.children) > 0 else []
        for node in self.children.values():
            nodes += node.get_children()

        return nodes


listing = False
topLevel = None
currDirectory = None
with open("C:\\Users\\User\\Downloads\\advent.txt") as file:
    for line in file:
        line = line.strip()
        if line.startswith("$"):
            line = line[2:]
            listing = False

            if line.startswith("cd"):
                directory = line.replace("cd ", "")
                if directory == "..":
                    currDirectory = currDirectory.parent
                    continue

                if currDirectory is None:
                    node = Node(currDirectory, directory)
                    currDirectory = node
                    topLevel = node
                    continue

                currDirectory = currDirectory.children[directory]

            if line == "ls":
                listing = True

            continue

        if listing:
            parts = line.split(" ")
            if parts[0] == "dir":
                currDirectory.children[parts[1]] = (Node(currDirectory, parts[1]))
            else:
                currDirectory.size += int(parts[0])

target = 30000000 - (70000000 - topLevel.get_size())
candidate = topLevel

for directory in topLevel.get_children():
    size = directory.get_size()
    if target < size < candidate.get_size():
        candidate = directory

print(candidate.get_size())
