from typing import Optional

class Solution:
    
    # O(n^2)
    def oddNumberTimes(self, nums: list[int]) -> Optional[int]:
        return next((i for i in nums if nums.count(i) % 2 != 0), None) 
    
    # O(n)
    


if __name__ == '__main__':
    print(Solution().oddNumberTimes([3, 1, 3]))  # 1