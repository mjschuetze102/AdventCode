import itertools


class Node:

    def __init__(self):
        self._antinode = False

    @property
    def antinode(self):
        return self._antinode

    def put_antinode(self):
        self._antinode = True

    def __str__(self):
        if self._antinode:
            return "#"

        return "."

    def __repr__(self):
        return self.__str__()


grid, antennas = [], {}
with open("/home/user/Downloads/advent.txt") as file:
    for line in file:
        grid.append([])
        for cell in line.strip():
            grid[-1].append(Node())

            if (cell != "."):
                antennas.setdefault(cell, []).append([len(grid) - 1, len(grid[-1]) - 1])


def find_antinode(point1, point2):
    return [2 * point1[0] - point2[0], 2 * point1[1] - point2[1]]


for group in antennas:
    for pair in itertools.permutations(antennas[group], 2):
        antinode = find_antinode(pair[0], pair[1])
        if 0 <= antinode[0] < len(grid) and 0 <= antinode[1] < len(grid[0]):
            grid[antinode[0]][antinode[1]].put_antinode()

print(sum(cell.antinode for row in grid for cell in row))
