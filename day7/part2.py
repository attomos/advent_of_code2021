from collections import Counter
from pathlib import Path


inp = Path("input.txt")
# inp = Path("sample.txt")

numbers = [int(line) for line in inp.read_text().split(",")]


# counter = Counter(numbers)
# most_common = counter.most_common()
# breakpoint()

# _, top = most_common[0]

# to_try = list(range(min(numbers), max(numbers)))

# average : )
to_try = [int(sum(numbers) / len(numbers))]


def calc(a, b):
    s = 0
    y = 0
    if b > a:
        a, b = b, a
    for _ in range(a, b - 1, -1):
        s += y
        y += 1

    return s


fuels = []
for t in to_try:
    fuel = 0
    for n in numbers:
        fuel += calc(n, t)
    fuels.append(fuel)


print(min(fuels))
