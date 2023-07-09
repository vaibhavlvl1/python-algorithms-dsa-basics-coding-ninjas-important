# simplest code for spiral print of following matrix


mat = [[1,2,3,4],
       [6,7,8,9],
       [11,12,13,14],
       [16,17,18,19],
       [21,22,23,24]]


def spiral_print(mat,rows,cols):
    a = 0
    b = 0

    while a<cols and b<rows:

        # top row
        for i in range(a,cols):
            print(mat[b][i])
        b+=1

        # left column
        for j in range(b,rows):
            print(mat[j][cols-1])
        cols-=1

        # bottom row
        for k in range(cols-1,a-1,-1):
            print(mat[rows-1][k])
        rows-=1

        # right column
        for l in range(rows-1,b-1,-1):
            print(mat[l][a])
        a+=1

        





# main

spiral_print(mat,5,4)