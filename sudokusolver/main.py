
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None,None

def is_valid(puzzle,guess,row,col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_val=[puzzle[i][col] for i in range(9)]
    if guess in col_val: 
        return False
    row_start = (row // 3) #1//3 = 0 5//3 = 1
    col_start = (col // 3)
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c] == guess:
                return False
    return True

    # col_val.append(puzzle[i][col])
    #col_val
        
def solve_sudoku(puzzle):
    row ,col = find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess

            if solve_sudoku(puzzle):
                return True
        puzzle[row][col]=-1

    return False

if __name__ == '__main__':
    sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
    print(solve_sudoku(sudoku_board))
    print(sudoku_board)

