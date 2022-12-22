import re
from math import floor


class Monkey:
    def __init__(self, starting_items, operation, test, state_change_matrix):
        self._items = starting_items
        self._operation = operation
        self._test = test
        self._state_change_matrix = state_change_matrix

        self._items_inspected = 0

    def has_items(self):
        return len(self._items) > 0

    def inspect_item(self):
        self._items[0] = self._operation(self._items[0])
        self._items[0] = floor(self._items[0] / 3)

        self._items_inspected += 1

    def throw_item(self):
        return self._state_change_matrix[self._items[0] % self._test == 0], self._items.pop(0)

    def receive_item(self, item):
        self._items.append(item)

    @property
    def items_inspected(self):
        return self._items_inspected

    def __str__(self):
        return str(self._items)


instruction_matrix = {
    "Monkey": lambda load: load,
    "Starting items": lambda load: list(map(int, load.split(","))),
    "Operation": lambda load: lambda old: eval(load.split("=")[1]),
    "Test": lambda load: int(re.search(r'\d+', load)[0]),
    "If true": lambda load: int(re.search(r'\d+', load)[0]),
    "If false": lambda load: int(re.search(r'\d+', load)[0]),
}

params = {}
monkeys = []
with open("C:\\Users\\User\\Downloads\\advent.txt") as file:
    for line in file:
        line = [instruction.strip() for instruction in line.split(":")]

        if line[0] == '':
            continue

        if line[0].startswith("Monkey"):
            line = line[0].split(" ")

        params[line[0]] = (instruction_matrix[line[0]](line[1]))

        if len(params) == 6:
            monkeys.append(Monkey(params["Starting items"],
                                  params["Operation"],
                                  params["Test"],
                                  {
                                      True: params["If true"],
                                      False: params["If false"]
                                  }))

            params.clear()

for _ in range(20):
    for monkey in monkeys:
        while monkey.has_items():
            monkey.inspect_item()
            thrown_to, item = monkey.throw_item()
            monkeys[thrown_to].receive_item(item)

monkeys.sort(key=lambda monkey: monkey.items_inspected, reverse=True)
print(monkeys[0].items_inspected * monkeys[1].items_inspected)
