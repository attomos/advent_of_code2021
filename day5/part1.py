from collections import Counter
from pathlib import Path


inp = Path("input.txt")
# inp = Path("sample.txt")

lines = inp.read_text().splitlines()


pairs = []

for line in lines:
    a, b = line.split(' -> ')
    x1, y1 = [int(x) for x in a.split(',')]
    x2, y2 = [int(x) for x in b.split(',')]
    pairs.append(((x1, y1), (x2, y2)))


track = []
for pair in pairs:
    # print(pair)
    (a, b), (c, d) = pair

    if a == c or b == d:
        if b == d:
            step = 1 if a <= c else -1
            for i in range(a, c + step, step):
                # print(i, b)
                track.append((i, b))
        else:
            step = 1 if b <= d else -1
            for i in range(b, d + step, step):
                # print(a, i)
                track.append((a, i))
    # breakpoint()


counter = Counter(track)
# print(counter)
ans = 0
for x, y in counter.items():
    if y >= 2:
        ans += 1

print(ans)
