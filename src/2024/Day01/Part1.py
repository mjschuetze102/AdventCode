with open("/home/user/Downloads/advent.txt") as file:
    lists = [[], []]

    for line in file:
        items = line.strip()

        for index, val in enumerate(items.split()):
            lists[index].append(int(val))

    for lst in lists:
        lst.sort()

    difference = sum(abs(x - y) for x, y in zip(*lists))
    print(difference)
