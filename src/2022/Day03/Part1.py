total = 0

with open("C:\\Users\\User\\Downloads\\advent.txt") as file:
    for line in file:
        items = line.strip()

        first = items[:len(items)//2]
        second = items[len(items)//2:]

        value = 0
        for item in first:
            if item in second:
                value = ord(item)
                break

        if value > 97:
            value -= 96
        else:
            value -= 38

        total += value

print(total)
