#  can only handle matrices of powers of 2 e.g 1*1 or 2*2, 4*4

# there is a trick with divide and conquer: you dont actually have to divide the problem space into "actual" smaller spaces,
# pointers (lo or hi) or even N(length of the array) could be passed around
def matrix_multiplication (matrixA, matrixB):
    def ikjMatrixProduct(A, B):
        n = len(A)
        C = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for k in range(n):
                for j in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    def matrix_addition(A, B):
        n = len(A)
        C = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
        return C
    # for i in range(0, len(matrixA), 2):
    #     a = []
    #     for row in matrixA:
    #         a  = a + [row[i:i+2]]
    #         if len(a) == 2:
    #             print(a)
    #             a = []

    n  = len(matrixA)
    if n <= 2: 
        return ikjMatrixProduct(matrixA, matrixB)
    else:
            #initializing the new sub-matrices
        newSize = n // 2
        a11 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        a12 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        a21 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        a22 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

        b11 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        b12 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        b21 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        b22 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

        for i in range(0, newSize):
            for j in range(0, newSize):
                a11[i][j] = matrixA[i][j]  # top left
                a12[i][j] = matrixA[i][j + newSize] # top right
                a21[i][j] = matrixA[i + newSize][j] # bottom left
                a22[i][j] = matrixA[i + newSize][j + newSize] # bottom right

                b11[i][j] = matrixB[i][j]  # top left
                b12[i][j] = matrixB[i][j + newSize]  # top right
                b21[i][j] = matrixB[i + newSize][j]  # bottom left
                b22[i][j] = matrixB[i + newSize][j + newSize]  # bottom right



        c11 = matrix_addition(matrix_multiplication(a11, b11), matrix_multiplication(a12, b21))
        c12 = matrix_addition(matrix_multiplication(a11, b12), matrix_multiplication(a12, b22))
        c21 = matrix_addition(matrix_multiplication(a21, b11), matrix_multiplication(a22, b21))
        c22 = matrix_addition(matrix_multiplication(a21, b12), matrix_multiplication(a22, b22))



        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(newSize):
            for j in range(newSize):
                C[i][j] = c11[i][j]
                C[i][j + newSize] = c12[i][j]
                C[i + newSize][j] = c21[i][j]
                C[i + newSize][j + newSize] = c22[i][j]
        return C
                


    


result = matrix_multiplication( [[1, 2, 3, 4], 
                            [1, 2, 3, 4],
                            [1, 2, 3, 4],
                            [1, 2, 3, 4]   
                          ], 
                          [ [1, 2, 3, 4], 
                            [1, 2, 3, 4],
                            [1, 2, 3, 4],
                            [1, 2, 3, 4]  
                          ]  
                        )
print(result)