matrix = []

matrix.append([])
matrix.append([])


matrix[0].append('kevin')
matrix[0].append(2)

matrix[1].append(3)
matrix[1].append(4)

print([matrix[0][0], matrix[0][1]])

print(matrix)

for row in matrix:
    for column in row:
        print(column, end=" ")
    print(end="\n")
