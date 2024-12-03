from collections import defaultdict

with open("/home/user/Downloads/advent.txt") as file:
    collections = [[], defaultdict(int)]

    for line in file:
        items = line.strip()

        values = items.split()
        collections[0].append(int(values[0]))
        collections[1][int(values[1])] += 1

    difference = sum(x * collections[1][x] for x in collections[0])
    print(difference)
