from pathlib import Path


inp = Path("input.txt")
# inp = Path("sample.txt")

line = inp.read_text().split(",")
numbers = [int(e) for e in line]

print(numbers)

for d in range(256):
    new_day = []
    new_born = []
    for e in numbers:
        if e > 0:
            new_day.append(e - 1)
        else:
            new_day.append(6)
            # new_born.append(8)
    new_born = [8] * new_day.count(6)
    numbers = new_day + new_born

print(len(numbers))
