# sudoku solver



grid=[[0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],]



def is_safe(num, row, col):
    # if row is safe
    global grid

    for i in range(9):
        if grid[row][i]==num:
            return False
    # if column is safe
    for j in range(9):
        if grid[j][col]==num:
            return False
        

    # if small sector is safe

    yo = (row//3)*3
    xo = (col//3)*3

    for i in range(3):
        for j in range(3):
            if grid[yo+i][xo+j]==num:
                return False
            
    return True

def solve_sudoku():
    global grid

    for row in range(9):
        for col in range(9):
            if  grid[row][col] ==0:
                for num in range(1,10):
                    if is_safe(num,row,col):
                        grid[row][col]=num
                        solve_sudoku()

                        grid[row][col]=0
                return
            
    for row in grid:
        print(row)

    print("----------------------")
    return

solve_sudoku()


