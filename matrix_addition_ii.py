mat1 = [[1, 3], [2, 4]]
mat2 = [[5, 2], [1, 0]]

def matrix_addition(matrix1, matrix2):
    result = []
    row_count = 0
    for row in matrix1:
        col_count = 0
        for col in row:
            result[row_count][col_count] = matrix1[row_count][col_count] + matrix2[row_count][col_count]
            col_count += 1
        row_count += 1
    return result

print(matrix_addition(mat1, mat2)) 