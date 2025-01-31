from typing import Optional

class Solution:
    def missingRepeated(self, nums: list[int]) -> (Optional[int], Optional[int]): 
        repeat = None
        
        wanted = set()
        seen = set()
        for num in nums:
            if num in seen:
                repeat = num
            seen.add(num) 
            
            pre = num - 1
            post = num + 1
            wanted.add(pre)
            wanted.add(post)
            
            # number is in missing
            if num in wanted:
                wanted.remove(num)
            
            if pre in seen:
                wanted.remove(pre)
            elif post in seen:
                wanted.remove(post)
        # Remove 0
        wanted.remove(0)
        
        # Remove max(nums) + 1
        wanted.remove(max(nums) + 1)
        return next(iter(wanted)), repeat

if __name__ == '__main__':
    print(Solution().missingRepeated([3, 1, 3]))  # (2, 3)
    print(Solution().missingRepeated([4, 3, 6, 2, 1, 1]))  # (5, 1)