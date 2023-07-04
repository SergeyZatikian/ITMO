import numpy as np
from numpy import linalg as LA
import timeit


matrix = [[1, 2, 3], [0, 1, 2], [2, 3, 0]]

for i in range(len(matrix)):
    print(matrix[i])

print()

def inverse (matrix):
    def deter2(minor):
        return minor [0][0] * minor [1][1] - minor [0][1] * minor [1][0]
    def deter3(m):
        a = m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[1][0] * m[2][1] * m[0][2]
        b = m[2][0] * m[1][1] * m[0][2] + m[1][0] * m[0][1] * m[2][2] + m[2][1] * m[1][2] * m[0][0]

        return a - b
    i = len(matrix[0])
    j = len(matrix)
    det = deter3(matrix) if i == 3 and j == 3 else 0
    if i == 3 and j == 3 and det != 0:
        result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        for strok in range(3):
            for el in range(3):
                matrix_copy = [a.copy () for a in matrix] 
                matrix_copy.pop(strok) 
                for st in range (2):
                    matrix_copy [st].pop(el)
                if (strok + el) % 2 == 0: 
                    k = 1
                else: 
                    k=-1
                result[strok][el] = deter2(matrix_copy) * k/det 
        return result
    else:
        return "Error"
for i in range(len(inverse(matrix))):
    print(inverse(matrix)[i])
print()
def inverse_np (matrix):
    mat = np.array (matrix)
    return np.linalg.inv (mat)
print(inverse_np(matrix))

st = timeit.default_timer()
inverse(matrix)
t1 = timeit.default_timer()-st
st = timeit.default_timer()
np.linalg.inv(matrix)
t2 = timeit.default_timer()-st

print(t1)
print(t2)
print(t1-t2)