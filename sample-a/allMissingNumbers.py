class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
            print(nums)
        print(nums)
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
            print(res)
    
    def findMissing(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            correct_pos = nums[i] - 1
            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        print(nums)
        missing = []
        for i in range(n):
            if nums[i] != i + 1:
                missing.append(i + 1)
        return missing

if __name__ == '__main__':
    solution = Solution()
    # print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]
    print(solution.findMissing([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]