def get_matrix(n,m,value):
    matrix = []
    for row_i in range(n):
        matrix.append([])
        for _ in range(m):
            matrix[row_i].append(value)
    return matrix


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
