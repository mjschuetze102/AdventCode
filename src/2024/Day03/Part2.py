from functools import reduce
import math
import re

value = 0
with open("/home/user/Downloads/advent.txt") as file:
    items = "".join([line.strip() for line in file])
    items = items.split("don't()")
    items = items[0] + "".join(["".join(item.split("do()")[1:]) for item in items[1:]])

    operations = re.findall("mul\\((\\d{1,3},\\d{1,3})\\)", items)
    value += reduce(lambda acc, curr: acc + math.prod([int(x) for x in curr.split(",")]), operations, 0)

print(value)
