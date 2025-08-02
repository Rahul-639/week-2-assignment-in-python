def count_zeros(matrix):
    n = len(matrix)
    count = 0
    row = 0
    col = n - 1

    while row < n and col >= 0:
        if matrix[row][col] == 0:
            count += (col + 1)
            row += 1
        else:
            col -= 1
    return count

# Example
A = [[0, 0, 0], [0, 0, 1], [0, 1, 1]]
print("Count of Zeros:", count_zeros(A))
