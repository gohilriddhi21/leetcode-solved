class Solution:
    def largest_rectangle_area(self, heights: list[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []

        for i in range(n):
            start = i
            while stack and (i==n or heights[i] < stack[-1][1]):
                ind, val = stack.pop()
                max_area = max(max_area, val*(i-ind))
                start = ind
            stack.append((start, heights[i]))
        
        for i, h in stack:
            max_area = max(max_area, h*(n-i))
        
        return max_area

if __name__ == '__main__':
    heights = [7,1,7,2,2,4]
    heights2 = [1,3,7]
    print(Solution().largest_rectangle_area(heights2)) 