from collections import defaultdict
from pathlib import Path


inp = Path("input.txt")
# inp = Path("sample.txt")

lines = inp.read_text().splitlines()

draws = []

boards = []
board = []
for i, line in enumerate(lines):
    if i == 0:
        draws = [int(d) for d in line.split(",")]

    if len(line.strip()) == 0 or i == len(lines) - 1:
        if i == len(lines) - 1:
            board.append([(int(v), False) for v in line.split()])
        if len(board):
            boards.append(board)
        board = []
    elif i != 0:
        board.append([(int(v), False) for v in line.split()])

# print(draws)

# for board in boards:
#     print(board)


def check(boards):
    for board in boards:
        cols = defaultdict(list)
        unmarked = []

        for i in range(5):
            for j in range(5):
                if board[i][j][1] == False:
                    unmarked.append(board[i][j][0])

        for i in range(5):
            for j in range(5):
                cols[j].append(board[i][j])
            row_value = [x[0] for x in board[i]]
            row_check = [x[1] for x in board[i]]
            if all([v == True for v in row_check]):
                return True, unmarked

        for col_index, col in cols.items():
            col_value = [x[0] for x in col]
            col_check = [x[1] for x in col]
            if all([v == True for v in col_check]):
                return True, unmarked

    return False, unmarked

def fill():
    for draw in draws:
        for board in boards:
            # fill
            for i in range(5):
                for j in range(5):
                    if board[i][j][0] == draw:
                        board[i][j] = (board[i][j][0], True)
                        check_result, unmarked = check(boards)
                        if check_result:
                            print(unmarked)
                            print(sum(unmarked) * draw)
                            print(f"bingo at {draw}")
                            return

fill()
