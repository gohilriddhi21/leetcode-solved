class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # return len(set(nums)) < len(nums)
        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    print(Solution().hasDuplicate([1,1]))  # True