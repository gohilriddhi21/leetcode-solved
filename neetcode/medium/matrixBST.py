class Solution:
    
    # Time: O(m + n)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) 

        l = 0
        r = n - 1
        while l < m and r >= 0:
            if target == matrix[l][r]:
                return True

            elif target > matrix[l][r]:
                l += 1
            
            else:
                r -= 1
        return False

    # Time: O(log(mn))
    def searchMatrix_2(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(Solution().searchMatrix(matrix, target)) # True

    target = 20
    print(Solution().searchMatrix(matrix, target)) # False

    matrix = [[-5]]
    target = -5
    print(Solution().searchMatrix(matrix, target)) # True

    target = -2
    print(Solution().searchMatrix(matrix, target)) # False

    matrix = [[1,4],[2,5]]
    target = 2
    print(Solution().searchMatrix_2(matrix, target)) # True

    target = 3
    print(Solution().searchMatrix_2(matrix, target)) # False

    matrix = [[1,3,5]]
    target = 3
    print(Solution().searchMatrix_2(matrix, target)) # True

    target = 4
    print(Solution().searchMatrix_2(matrix, target)) # False
