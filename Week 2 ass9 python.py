def is_identity_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j and matrix[i][j] != 1:
                return False
            elif i != j and matrix[i][j] != 0:
                return False
    return True

# Example
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

if is_identity_matrix(matrix):
    print("It is an Identity Matrix.")
else:
    print("It is NOT an Identity Matrix.")
