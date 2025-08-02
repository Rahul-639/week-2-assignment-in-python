def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]
    return total

# Example
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Diagonal Sum:", diagonal_sum(mat))  # Output: 15
