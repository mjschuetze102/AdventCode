import itertools


value = 0
operators = ["+", "*"]
with open("/home/user/Downloads/advent.txt") as file:
    for line in file:
        items = line.split(":")
        result, terms = items[0], items[1].strip().split()

        equations = [terms[0]]
        for i in range(1, len(terms)):
            equations = [str(eval("".join(equation))) for equation in itertools.product(equations, operators, [terms[i]])]

        if any([equation == result for equation in equations]):
            value += int(result)

print(value)
