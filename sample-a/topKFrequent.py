from collections import Counter, defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        print(counts)
        
        buckets = defaultdict(list)
        for i,v in counts.items():
            buckets[v].append(i)
        print(buckets)

        
        result = []
        for freq in sorted(buckets.keys(), reverse=True): 
            result.extend(buckets[freq])  
            print(result)
            if len(result) >= k:
                break

        return result[:k]

if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))