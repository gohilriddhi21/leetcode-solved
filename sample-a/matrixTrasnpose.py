from collections import deque

def rotate_matrix(mat):
    m, n = len(mat), len(mat[0])
    res = [[0] * m for _ in range(n)]

    # Transpose the matrix
    for i in range(m):
        for j in range(n):
            res[j][i] = mat[i][j]
            print(res)

    print("\nTranspose:\n")
    # Reverse each column (not row) of the result which is a n x m matrix
    for j in range(m):
        for i in range(n // 2):
            res[i][j], res[n - i - 1][j] = res[n - i - 1][j], res[i][j]
            print(res)
    
    return res


if __name__ == "__main__":
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    res = rotate_matrix(mat)
    
    for row in res:
        print(" ".join(map(str, row)))
