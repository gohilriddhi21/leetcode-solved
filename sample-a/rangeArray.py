class Solution:
    def rangeArray(self, nums:list[int], a:int, b:int) -> bool:
        for i in range(a, b+1):
            if i not in nums:
                return False
        return True
    

if __name__ == '__main__':
    print(Solution().rangeArray([1, 4, 5, 2, 7, 8, 3], 2,5)) # [0, 1, 2, 3, 4]