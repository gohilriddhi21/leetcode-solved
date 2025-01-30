class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
            elif(target < nums[mid]):
                r = mid - 1
            elif (target > nums[mid]):
                l = mid + 1
        return -1
    
if __name__ == "__main__":
    print(Solution().search([-1,0,2,4,6,8], 4))