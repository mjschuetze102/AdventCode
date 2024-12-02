import re


initializing = True
instructions = False

stacks = []
with open("C:\\Users\\User\\Downloads\\advent.txt") as file:
    for line in file:

        if not stacks:
            numStacks = len(line) // 4

            for i in range(numStacks):
                stacks.append([])

        if line == "\n":
            continue

        if line.startswith(" 1 "):
            for stack in stacks:
                stack.reverse()

            initializing = False
            instructions = True
            continue

        if initializing:
            inputs = [line[i + 1] for i in range(0, len(line), 4)]

            for index, item in enumerate(inputs):
                if item != " ":
                    stacks[index].append(item)

        if instructions:
            steps = [int(s) - 1 for s in re.findall(r'\d+', line)]

            amountToMove = steps[0] + 1
            fromIndex = steps[1]
            toIndex = steps[2]

            crates = stacks[fromIndex][-amountToMove:]
            stacks[fromIndex] = stacks[fromIndex][:-amountToMove]
            stacks[toIndex].extend(crates)

tops = [stack.pop() for stack in stacks]
print("".join(tops))
