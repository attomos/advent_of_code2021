from pathlib import Path
from collections import Counter


inp = Path("input.txt")
# inp = Path("sample.txt")

lines = inp.read_text().splitlines()

reports = []

for i in range(len(lines[0])):
    counter = Counter()
    reports.append(counter)

for line in lines:
    for i, c in enumerate(line):
        reports[i][c] += 1


gamma_rate = ""
epsilon_rate = ""
for r in reports:
    mc = r.most_common()
    most_common = mc[0][0]
    least_common = mc[-1][0]
    gamma_rate += most_common
    epsilon_rate += least_common

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
