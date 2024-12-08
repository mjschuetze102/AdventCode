grid = []
with open("/home/user/Downloads/advent.txt") as file:
    for line in file:
        grid.append(list(line.strip()))


def number_of_matches(grid, word, position):
    if grid[position[0]][position[1]] != word[1]:
        return 0

    length, height, width = len(word) // 2, len(grid), len(grid[0])
    if any([
        position[0] - (length) < 0,
        position[0] + (length) >= height,
        position[1] - (length) < 0,
        position[1] + (length) >= width
    ]):
        return 0

    directions_to_check = [[-1, -1], [-1, 1],  # noqa: E201
                           [ 1, -1], [ 1, 1]]  # noqa: E201

    if not all(value in ['M', 'S'] for value in [grid[position[0] + row][position[1] + col] for [row, col] in directions_to_check]):
        return 0

    if any([
        grid[position[0] - 1][position[1] - 1] == grid[position[0] + 1][position[1] + 1],
        grid[position[0] - 1][position[1] + 1] == grid[position[0] + 1][position[1] - 1]
    ]):
        return 0

    return 1


word_to_find = "MAS"

num = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == word_to_find[1]:
            num += number_of_matches(grid, word_to_find, [row, col])

print(num)
