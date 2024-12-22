memory = []
with open("/home/user/Downloads/advent.txt") as file:
    line = file.readline().strip()

    for i in range(len(line)):
        num = int(line[i])
        memory.extend([i // 2] * num if i % 2 == 0 else ["."] * num)

reverse = memory[::-1]

i = j = 0
while i < len(memory) - j:
    check = i + j
    i += memory[i] != "."
    j += reverse[j] == "."

    if i + j != check:
        continue

    memory[i] = reverse[j]
    memory[-j - 1] = "."

    i += 1
    j += 1

print(sum(memory[i] * i for i in range(memory.index("."))))
