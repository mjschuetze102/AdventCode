import itertools


page_requirements = {}
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline().strip()):
        key, value = line.split("|")
        page_requirements.setdefault(key, []).append(value)

    sum = 0
    for line in file:
        line = line.strip().split(",")

        req_checks = itertools.chain.from_iterable([[page not in page_requirements.get(other_page, []) for other_page in line[i + 1:]] for i, page in enumerate(line)])
        if all(req_checks):
            continue

        i = 0
        while i < len(line):
            prereqs = [j for j in range(i + 1, len(line)) if line[i] in page_requirements.get(line[j], [])]
            if prereqs:
                element = line.pop(i)
                line.insert(prereqs[-1], element)
                i -= 1

            i += 1

        sum += int(line[len(line) // 2])

    print(sum)
