def spiral_matrix(matrix):  # sourcery skip: for-append-to-extend, switch
    if not matrix or not matrix[0]:  # Handle empty matrix case
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    direction = 0  # 0: right, 1: down, 2: left, 3: up
    result = []

    while top <= bottom and left <= right:
        if direction == 0:  # Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
        elif direction == 1:  # Down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
        elif direction == 2:  # Left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        elif direction == 3:  # Up
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        direction = (direction + 1) % 4

    return result


# Example usage:
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(spiral_matrix(matrix1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
print(spiral_matrix(matrix2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
