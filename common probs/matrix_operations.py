class matrix_ops:
    def __init__(self):
        matrix1 = NaN
        matrix2 = NaN
        result = NaN

    @classmethod
    def set_const_var(cls):
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix2 = [[19, 18, 17], [16, 15, 14], [13, 12, 11]]
        result = [[0,0,0],[0,0,0],[0,0,0]]

    def operation(matrix1, matrix2):
        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                result[i][j] = matrix2[i][j] - matrix1[i][j]
        for r in result:
            print(result)


operation(matrix1, matrix2)



matrix1 = [[10, 11, 12],
	   [13, 14, 15],
	   [16, 17, 18]]
matrix2 = [[1, 2, 3],
	   [4, 5, 6],
	   [7, 8, 9]]
rmatrix = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] - matrix2[i][j]
for r in rmatrix:
    print(r)