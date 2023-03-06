def isTriangular(mat, n):#function for determining if the matrix is upper triangular or lower triangular
    upperT = True
    lowerT = True

    for i in range(n):
        for j in range(n):
            if i < j:#when row is less than column
                if j+1 < n:
                    if mat[i][j+1] != 0:#when it is above the main diagonal
                        lowerT = False
            if i > j:#when column is greater than row
                if i+1 < n:
                    if mat[i+1][j] != 0:#when it is below the main diagonal
                        upperT = False
    return upperT, lowerT

n = int(input("Enter the size of the matrix: "))
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        ask = int(input("Enter element [" + str(i+1) + "," + str(j+1) + "] of the matrix: "))
        row.append(ask)
    matrix.append(row)

upperTriangular, lowerTriangular = isTriangular(matrix, n)

if upperTriangular == True and lowerTriangular == True:
    print("This matrix is both lower and upper triangular.")
elif upperTriangular == True and lowerTriangular == False:
    print("This matrix is upper triangular.")
elif upperTriangular == False and lowerTriangular == True:
    print("This matrix is lower triangular.")
else:
    print("This matrix is neither upper nor lower triangular.")