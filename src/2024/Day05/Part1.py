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
            sum += int(line[len(line) // 2])

    print(sum)
