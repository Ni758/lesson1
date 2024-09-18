def get_matrix(n,m,value):
    matrix = []
    for row_i in range(n):
        matrix.append([])
        print(matrix)
        for _ in range(m):
            matrix[row_i].append(value)
            print(matrix)
    return matrix


get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
