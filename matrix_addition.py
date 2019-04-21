mat1 = [[1, 3], [2, 4]]
mat2 = [[5, 2], [1, 0]]


def matrix_addition(matrix1, matrix2):
    row1 = [matrix1[0][0] + matrix2[0][0], matrix1[0][1] + matrix2[0][1]]
    row2 = [matrix1[1][0] + matrix2[1][0], matrix1[1][1] + matrix2[1][1]]
    result = [row1, row2]
    return result

print(matrix_addition(mat1, mat2))
