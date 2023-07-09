# N queens problem

def nqn(n):
    board = [[0]*n for i in range(n)]
    posDiag = set()
    negDiag = set()
    cols = set()

    def backtrack(r):
        if r==n:
            for row in board:
                print(row)

            print("---------------------")
            return
        for c in range(n):
            if c in cols or r+c in posDiag or r-c in negDiag:
                continue
            else:
                board[r][c] = 1
                posDiag.add(r+c)
                negDiag.add(r-c)
                cols.add(c)

                backtrack(r+1)

                board[r][c] = 0
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                cols.remove(c)

    backtrack(0)




# program main

nqn(4)

