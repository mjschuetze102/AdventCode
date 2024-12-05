safe_reports = 0

with open("/home/user/Downloads/advent.txt") as file:
    for line in file:
        items = line.strip()

        report = [int(x) for x in items.split()]
        sign = (report[0] - report[1]) / abs(report[0] - report[1]) if report[0] != report[1] else 1

        safe_reports += all(1 <= (report[index] - report[index + 1]) * sign <= 3 for index in range(len(report) - 1))

print(safe_reports)
