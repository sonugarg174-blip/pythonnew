"""N-Queens using backtracking. Try changing N to 4, 5, or 8."""

N = 4
board = [-1] * N  # board[row] stores the column of that row's queen


def is_safe(row, col):
    for earlier_row in range(row):
        earlier_col = board[earlier_row]
        # Same column or same diagonal means attack.
        if earlier_col == col:
            return False
        if abs(earlier_col - col) == abs(earlier_row - row):
            return False
    return True


def solve(row):
    if row == N:
        return True  # A queen was safely placed in every row.

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1  # Backtrack and try another column.
    return False


if solve(0):
    print("One solution for", N, "queens:")
    for row in range(N):
        print(" ".join("Q" if board[row] == col else "." for col in range(N)))
else:
    print("No solution exists for N =", N)
