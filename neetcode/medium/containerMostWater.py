class Solution:
    def maxArea_naive(self, heights: list[int]) -> int:
        res = {}
        max_val = 0
        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                area = min(heights[l], heights[r]) * (r-1)
                res[f"{heights[l]}-{heights[r]}"] = max(max_val, area)
                if area > max_val:
                    max_val = area
        return res

    def maxArea(self, heights: list[int]) -> int:
        i, j = 0, len(heights) - 1
        
        max_area = float('-inf')
        rods = ()
        while i < j:
            w = (j-i) * min(heights[i], heights[j])
            max_area = max(max_area, w)
            rods = (i, j) if w == max_area else rods
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return (heights[rods[0]], heights[rods[1]]), max_area


if __name__ == "__main__":
    heights = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(heights))