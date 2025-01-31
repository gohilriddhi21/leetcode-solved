class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

if __name__  == "__main__":
    sol = Solution()
    # print(sol.productExceptSelf([1,2,3,4])) # [24,12,8,6]
    # print(sol.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
    # print(sol.productExceptSelf([1,2,3,4,5,6,7,8,9,10])) # [3628800,1814400,1209600,907200,725760,604800,518400,453600,403200,362880]
    print(sol.productExceptSelf([10, 3, 5, 6, 2])) #  [180, 600, 360, 300, 900]