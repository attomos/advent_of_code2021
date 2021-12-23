from collections import Counter
from pathlib import Path


inp = Path("input.txt")
# inp = Path("sample.txt")

numbers = [int(line) for line in inp.read_text().split(",")]


counter = Counter(numbers)



most_common = counter.most_common()

_, top = most_common[0]

to_try = []

for k, v in most_common:
    to_try.append(k)

# to_try = [round(sum(numbers) / len(numbers))]
# print(sum(numbers) / len(numbers))
# print(to_try)

fuels = []
for t in to_try:
    fuel = 0
    for n in numbers:
        fuel += abs(n - t)
    fuels.append(fuel)


print(min(fuels))
