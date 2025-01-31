class Solution:
    def eq(self, nums: list[int]) -> int:
        ls, rs = 0, 0
        l = 0
        r = len(nums) - 1
        while l < r:
            ls = ls + nums[l]
            rs = rs + nums[r]
            if ls == rs:
                return l+1
            l+=1
            r-=1
        return -1

if __name__ == "__main__":
    print(Solution().eq([1, 2, 0, 3]))  # 2
    print(Solution().eq([1, 1, 1, 1]))  # -1