
matrix = [[],[],[]]

def rowOP(down, up, k):
    global matrix
    for p n range(len(matrix[0])):
        matrix[down][up] -= k*matrix[up][p]

def Gauss():
    global matrix
    for i in range(len(matrix)):
        rowOp(i,i,(1-1/matrix[i][i]))
        for j in range(i, len(matrix)):
            if i != j:
                rowOp(j,i,matrix[j][i])

Gauss()
for i in matrix:
    print(i)
