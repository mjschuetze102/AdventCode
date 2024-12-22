memory = []
with open("/home/user/Downloads/advent.txt") as file:
    line = file.readline().strip()

    for i in range(len(line)):
        num = int(line[i])
        memory.append((i // 2, num) if i % 2 == 0 else (".", num))

reverse = memory[::-1]

for i in range(0, len(reverse), 2):
    k = memory.index(reverse[i])
    for j in range(1, k, 2):
        if reverse[i][1] <= memory[j][1]:
            k -= 1
            memory[k] = (memory[k][0], sum(x[1] for x in memory[k:k + 3]))
            memory[k + 1:k + 3] = []

            memory[j] = (memory[j][0], memory[j][1] - reverse[i][1])
            memory[j:j + 1] = [(".", 0), reverse[i], memory[j]]
            break

memory = [val for val, num in memory for _ in range(num)]
print(sum(memory[i] * i for i in range(len(memory)) if memory[i] != "."))
