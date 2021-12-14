from pathlib import Path


inp = Path("input.txt")
# inp = Path("sample.txt")

numbers = [int(line) for line in inp.read_text().splitlines()]

inc = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        inc += 1

print(inc)
