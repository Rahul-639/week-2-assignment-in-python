def multiply_polynomials(A, B):
    n, m = len(A), len(B)
    result = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            result[i + j] += A[i] * B[j]
    return result

# Example
A = [1, 2]  # 1 + 2x
B = [3, 4]  # 3 + 4x

print("Polynomial A:", A)
print("Polynomial B:", B)

product = multiply_polynomials(A, B)
print("Product Polynomial Coefficients:", product)
