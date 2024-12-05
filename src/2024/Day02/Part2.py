safe_reports = 0

with open("/home/user/Downloads/advent.txt") as file:
    for line in file:
        items = line.strip()

        report = [int(x) for x in items.split()]
        troper = report[::-1]

        sign = next((report[0] - value) / abs(report[0] - value) for value in report if value != report[0])
        bad_reading = next((index for index in range(len(report) - 1) if not 1 <= (report[index] - report[index + 1]) * sign <= 3), -1)
        report.pop(bad_reading) if 1 <= (report[bad_reading - 1] - report[bad_reading + 1]) * sign <= 3 else report.pop(bad_reading + 1)

        ngis = next((troper[0] - value) / abs(troper[0] - value) for value in troper if value != troper[0])
        gnidaer_dab = next((index for index in range(len(troper) - 1) if not 1 <= (troper[index] - troper[index + 1]) * ngis <= 3), -1)
        troper.pop(gnidaer_dab) if 1 <= (troper[gnidaer_dab - 1] - troper[gnidaer_dab + 1]) * sign <= 3 else troper.pop(gnidaer_dab + 1)

        safe_reports += (all(1 <= (report[index] - report[index + 1]) * sign <= 3 for index in range(len(report) - 1)) or all(1 <= (troper[index] - troper[index + 1]) * ngis <= 3 for index in range(len(troper) - 1)))

print(safe_reports)
