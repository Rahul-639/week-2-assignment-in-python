def multiply_polynomials(A, B):
    n = len(A)
    m = len(B)
    result = [0] * (n + m - 1)

    for i in range(n):
        for j in range(m):
            result[i + j] += A[i] * B[j]
    return result

# Example
A = [5, 0, 10, 6]
B = [1, 2, 4]
print("Product of polynomials:", multiply_polynomials(A, B))
