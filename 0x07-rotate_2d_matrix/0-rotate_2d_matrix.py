#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    n = len(matrix)

    # First, transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Next, reverse each row to rotate the matrix clockwise
    for i in range(n):
        matrix[i] = matrix[i][::-1]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)

for row in matrix:
    print(row)
