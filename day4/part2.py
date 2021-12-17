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

def viz(board):
    s = ""
    for i in range(5):
        for j in range(5):
            if board[i][j][1]:
                s += f"({board[i][j][0]})    "
            else:
                s += f"{board[i][j][0]}     "
        s += "\n"
    print(s)


def check(boards):
    for board in boards:
        a, b = check_board(board)
        if a:
            return a, b

    return False, []


def check_board(board):
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
            # print(row_value)
            # breakpoint()
            return True, unmarked

    for col_index, col in cols.items():
        col_value = [x[0] for x in col]
        col_check = [x[1] for x in col]
        if all([v == True for v in col_check]):
            return True, unmarked

    return False, unmarked


won_board_ids = []
def fill():
    for draw in draws:
        for board_id, board in enumerate(boards):
            # fill
            for i in range(5):
                for j in range(5):
                    if board[i][j][0] == draw:
                        board[i][j] = (board[i][j][0], True)
                        check_result, unmarked = check_board(board)
                        if check_result:
                            if not board_id in won_board_ids:
                                print("")
                                print("")
                                viz(board)
                                won_board_ids.append(board_id)
                                print(won_board_ids)
                                print(unmarked)
                                print(sum(unmarked) * draw)
                                print(f"bingo at {draw}")

fill()
