class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [ seen[diff] , i ]
            else:
                seen[nums[i]] = i 
            print(seen)
        return []

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 3, 4, 5, 6, 7], 9))
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))
