from pathlib import Path


inp = Path("input.txt")
# inp = Path("sample.txt")

numbers = [int(line) for line in inp.read_text().splitlines()]

inc = 0


counter = 0
ss = 0

ss_list = []
for i in range(len(numbers) - 2):
    ss = numbers[i] + numbers[i + 1] + numbers[i + 2]
    ss_list.append(ss)


for i in range(1, len(ss_list)):
    if ss_list[i] > ss_list[i - 1]:
        inc += 1

# print(ss_list)
print(inc)
