def read_file():
    board_num = 0
    boards = []
    rows = []
    with open("input_day4.txt", "r") as input_file:
        row_num = 0
        for line in input_file:
            if board_num == 0:
                print(line)
                draws = [int(i) for i in line.strip().split(",")]
                board_num += 1
            elif row_num > 0:
                row_temp = [i for i in line.strip().split(" ")]
                row = []
                for item in row_temp:
                    if item != '':
                        row.append(int(item))
                rows.append(row)
                row_num += 1
                if row_num % 6 == 0:
                    boards.append(rows)
                    rows = []
                    board_num += 1
                    row_num = 0
            else:
                row_num += 1
    return draws, boards


def check_rows(board, drawn):
    for row in range(len(board)):
        all_in = True
        for col in range(len(board[row])):
            if all_in and board[row][col] not in drawn:
                all_in = False
        if all_in:
            return True
    return False


def check_columns(board, drawn):
    for col in range(len(board[0])):
        all_in = True
        for row in range(len(board)):
            if all_in and board[row][col] not in drawn:
                all_in = False
        if all_in:
            return True
    return False


def check_board(board, drawn):
    return check_rows(board, drawn) or check_columns(board, drawn)


def calculate_score(board, drawn):
    unmarked_sum = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] not in drawn:
                unmarked_sum += board[row][col]
    return unmarked_sum * drawn[-1]


def play_to_win(boards, draws):
    bingo = False
    draw_counter = 1
    while not bingo and draw_counter <= len(draws):
        for board in boards:
            if check_board(board, draws[0:draw_counter]):
                bingo = True
                score = calculate_score(board, draws[0:draw_counter])
                return score
        draw_counter += 1


def play_to_lose(boards, draws):
    bingo = True
    draw_counter = len(draws)
    while bingo and draw_counter >= 0:
        for board in boards:
            if not check_board(board, draws[0:draw_counter]):
                bingo = False
                score = calculate_score(board, draws[0:draw_counter+1])
                print(draw_counter)
                return score
        draw_counter -= 1


if __name__ == '__main__':
    draws, boards = read_file()
    print(draws[0:10])
    print(check_board(boards[0], draws[0:50]))
    print(calculate_score(boards[0], draws[0:50]))
    print(play_to_win(boards, draws))
    print(play_to_lose(boards, draws))


