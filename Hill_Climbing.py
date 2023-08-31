def calculate_conflicts(binary_board):
    conflicts = 0
    n = len(binary_board)

    for row in binary_board:
        queen_count = row.count(1)
        if queen_count > 1: # assuming that 1 queen per row if there is no conflict
            conflicts += queen_count - 1

    # Count diagonal conflicts
    for col in range(n):
        main_diag_count = 0
        anti_diag_count = 0
        for row in range(n):
            if binary_board[row][col] == 1:
                if row + col < n:
                    main_diag_count += 1
                else:
                    anti_diag_count += 1

        if main_diag_count > 1:
            conflicts += main_diag_count * (main_diag_count - 1) // 2
        if anti_diag_count > 1:
            conflicts += anti_diag_count * (anti_diag_count - 1) // 2

    return conflicts


if __name__ == "__main__":
    binary_board = [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [1, 0, 0, 0]]
    res = calculate_conflicts(binary_board)
    print(res)
