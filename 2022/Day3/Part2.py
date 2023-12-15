total = 0

first, second, third = [], [], []
with open("C:\\Users\\User\\Downloads\\advent.txt") as file:
    for line in file:
        items = line.strip()

        if not first:
            first = items
            continue
        elif not second:
            second = items
            continue
        else:
            third = items

        value = 0
        for item in first:
            if item in second and item in third:
                value = ord(item)
                break

        first, second, third = [], [], []

        if value > 97:
            value -= 96
        else:
            value -= 38

        total += value

print(total)
