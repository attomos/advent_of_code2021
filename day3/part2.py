from pathlib import Path
from collections import Counter, defaultdict


inp = Path("input.txt")
# inp = Path("sample.txt")

lines = inp.read_text().splitlines()


def calc(lines, index, variant: str):
    d = defaultdict(list)
    counter = Counter()
    for line in lines:
        d[line[index]].append(line)
        counter[line[index]] += 1

    mc = counter.most_common()
    most_common = mc[0][0]
    least_common = mc[-1][0]

    if mc[0][1] == mc[-1][1]:
        if variant == "oxygen":
            new_lines = d["1"]
        else:
            new_lines = d["0"]
    elif variant == "oxygen":
        new_lines = d[most_common]
    else:
        new_lines = d[least_common]

    if len(new_lines) == 1:
        return new_lines[0]

    return calc(new_lines, index + 1, variant)


oxygen_rate = calc(lines, 0, variant="oxygen")
oxygen_rate = int(oxygen_rate, 2)

co2_rate = calc(lines, 0, variant="co2")
co2_rate = int(co2_rate, 2)

print(oxygen_rate * co2_rate)
