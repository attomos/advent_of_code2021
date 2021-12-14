from pathlib import Path


inp = Path("input.txt")
# inp = Path("sample.txt")

lines = inp.read_text().splitlines()

position = 0
depth = 0

for line in lines:
    command, unit = line.split(" ")
    unit = int(unit)
    if command == "forward":
        position += unit
    elif command == "down":
        depth += unit
    elif command == "up":
        depth -= unit

print(position * depth)
