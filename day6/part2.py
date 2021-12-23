# Couldn't solve part 2 myself
# I use the solution from this comment.
# https://www.reddit.com/r/adventofcode/comments/r9z49j/2021_day_6_solutions/hotaz5z/?utm_source=reddit&utm_medium=web2x&context=3
from pathlib import Path


inp = Path("input.txt")
# inp = Path("sample.txt")

line = inp.read_text().split(",")
numbers = [int(e) for e in line]

current_states = {
    0: numbers.count(0),
    1: numbers.count(1),
    2: numbers.count(2),
    3: numbers.count(3),
    4: numbers.count(4),
    5: numbers.count(5),
    6: numbers.count(6),
    7: numbers.count(7),
    8: numbers.count(8),
}

for d in range(256):
    next_states = {
        0: current_states[1],
        1: current_states[2],
        2: current_states[3],
        3: current_states[4],
        4: current_states[5],
        5: current_states[6],
        6: current_states[7],
        7: current_states[8],
        8: current_states[0],
    }

    if current_states[0] > 0:
        next_states[6] += current_states[0]
    
    current_states = next_states
    next_states = {}


total = 0
for fish in current_states:
    total += current_states[fish]


ans = sum(current_states.values())
print(ans)
