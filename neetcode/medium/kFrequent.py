from collections import defaultdict

class Solution:
    # Time complexity: O(n log n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = defaultdict(int)
        for n in nums:
            res[n] += 1
        
        result = []
        for key, v in sorted(res.items(), reverse=True):
            print(key, v)
            if k > 0:
                result.append(key)
                k -= 1
        return result

    # Time complexity: O(n)
    def topKFrequent_2(self, nums: list[int], k: int) -> list[int]:
        return 0
    
                 

if __name__ == "__main__":
    print(Solution().topKFrequent([1,2,2,3, 3, 3], 2))  # [1, 2]