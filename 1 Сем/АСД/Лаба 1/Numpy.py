import numpy as np
from numpy import linalg as LA
import timeit

matrix = [[1, 2, 3], [0, 1, 2]]

def transposition(matrix):
    Matrix = np.array (matrix)
    return Matrix.transpose ()

for i in range(len(transposition(matrix))):
    print(transposition(matrix)[i])

mat1 = [[3, 4],[5, 1]]
mat2 = [[8, 1],[2, 3]]

def multiplication(mat1, mat):
    mat_1 = np.array (mat1)
    mat_2 = np.array (mat2)
    return np.matmul (mat_1, mat_2)
for i in range(len(multiplication(mat1, mat2))):
    print((multiplication(mat1, mat2))[i])

def rang (matrix):
    mat = np.array (matrix)
    return np.linalg.matrix_rank(mat)
print(rang(matrix))
