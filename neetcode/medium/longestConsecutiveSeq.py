from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_length = 0
        nums = set(nums)
        for num in nums:
            if (num - 1) in nums:
                continue
            length = 1
            while num + length in nums:
                length += 1
            max_length = max(max_length, length)
        return max_length

if __name__ == "__main__":
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2])) # 4