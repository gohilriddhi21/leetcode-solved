class Solution:
    def rotateArray(self, nums: list[int]) -> list[int]:
        n = len(nums) 
        temp = nums[-1]
        for i in range(n-1, 0, -1):
            nums[i] =  nums[i-1]
        nums[0] = temp
        return nums


if __name__ == "__main__":
    print(Solution().rotateArray([1,2,3,4,5,6,7], 3))  # [5,6,7,1,2,3,4]