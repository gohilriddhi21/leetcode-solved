class Solution:
    # def addOne(self, nums:list[int]) -> list[int]:
    #     n = len(nums)
        
    #     carry = 0 
    #     j = 1
    #     for i in range(n-1, -1, -1):
    #         val = nums[i] + j + carry
    #         nums[i] = val % 10
    #         carry = val // 10
    #         j = 0
        
    #     if carry > 0:
    #         nums.insert(0, carry)
    #     return nums
    
    def addOne(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n - 1, -1, -1):
            nums[i] += 1  # Add 1 directly
            if nums[i] < 10:  # No carry
                return nums  # We're done!
            nums[i] %= 10  # Handle carry, set digit to 0

        # If we reach here, it means there was a carry all the way to the most significant digit
        nums.insert(0, 1) # Insert 1 at the beginning
        return nums

if __name__ == "__main__":
    print(Solution().addOne([9,9,9]))  # [1,2,4]