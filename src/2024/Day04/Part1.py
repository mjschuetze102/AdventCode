import itertools


grid = []
with open("/home/user/Downloads/advent.txt") as file:
    for line in file:
        grid.append(list(line.strip()))


def number_of_matches(grid, word, position):
    if grid[position[0]][position[1]] != word[0]:
        return 0

    directions_to_check = [[[-1, -1], [-1, 0], [-1, 1]],  # noqa: E201
                           [[ 0, -1],          [ 0, 1]],  # noqa: E201
                           [[ 1, -1], [ 1, 0], [ 1, 1]]]  # noqa: E201

    length, height, width = len(word), len(grid), len(grid[0])
    if position[0] - (length - 1) < 0:
        del directions_to_check[0]

    if position[0] + (length - 1) >= height:
        del directions_to_check[-1]

    if position[1] - (length - 1) < 0:
        directions_to_check = [group[1:] for group in directions_to_check]

    if position[1] + (length - 1) >= width:
        directions_to_check = [group[:-1] for group in directions_to_check]

    directions_to_check = list(itertools.chain.from_iterable(directions_to_check))

    matches = 0
    for [row, col] in directions_to_check:
        matches += all([grid[position[0] + row * i][position[1] + col * i] == word[i] for i in range(1, length)])

    return matches


word_to_find = "XMAS"

num = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == word_to_find[0]:
            num += number_of_matches(grid, word_to_find, [row, col])

print(num)
