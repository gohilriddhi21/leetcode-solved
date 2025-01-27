from collections import defaultdict
import heapq

class Solution:
    # # Time complexity: O(n log n)
    def topKFrequent_naive(self, nums: list[int], k: int) -> list[int]:
        res = defaultdict(int)
        for n in nums:
            res[n] += 1
        
        result = []
        for key, v in sorted(res.items(), reverse=True):
            # print(key, v)
            if k > 0:
                result.append(key)
                k -= 1
        return result

    # Time complexity: O(n)
    def topKFrequent_2(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
                
        # Heap
    def topKFrequent_heap(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        res.extend(heapq.heappop(heap)[1] for _ in range(k))
        return res

if __name__ == "__main__":
    print(Solution().topKFrequent_naive([1,2,2,3, 3, 3, 4, 4, 4, 5, 5, 5], 2))  # [1, 2]
    print(Solution().topKFrequent_2([1,2,2,3, 3, 3, 4, 4, 4, 5, 5, 5], 2))  # [1, 2]
    print(Solution().topKFrequent_heap([1,2,2,3, 3, 3, 4, 4, 4, 5, 5, 5], 2))  # [1, 2]