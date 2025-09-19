def next_box(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return (row, col)
    return False


def possible(puzzle, row, col, n):
    # global quiz
    for i in range(0, 9):
        if puzzle[row][i] == n and row != i:
            return False
    for i in range(0, 9):
        if puzzle[i][col] == n and col != i:
            return False

    row0 = (row) // 3
    col0 = (col) // 3
    for i in range(row0 * 3, row0 * 3 + 3):
        for j in range(col0 * 3, col0 * 3 + 3):
            if puzzle[i][j] == n and (i, j) != (row, col):
                return False
    return True


def is_solvable(puzzle):
    val = next_box(puzzle)
    if val is False:
        return True
    else:
        row, col = val
        for n in range(1, 10):  # n is the possible solution
            if possible(puzzle, row, col, n):
                puzzle[row][col] = n
                if is_solvable(puzzle):
                    return True
                else:
                    puzzle[row][col] = 0
        return


def print_solution(puzzle):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("....................")

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")

            if col == 8:
                print(puzzle[row][col])
            else:
                print(str(puzzle[row][col]) + " ", end="")


def solve_sudoku(puzzle):
    if is_solvable(puzzle):
        print_solution(puzzle)
    else:
        print("Solution don't exist. Model misread digits")
