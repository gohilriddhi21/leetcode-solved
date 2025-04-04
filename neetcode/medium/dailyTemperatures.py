from collections import defaultdict

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)
        return res

    def mono_decreasing_stack(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * len(temperatures)
        
        stack=[]
        for i in range(n):
            while stack and stack[-1][1] < temperatures[i]:
                idx, _ = stack.pop()
                res[idx] = i - idx
            stack.append((i,temperatures[i]))
        return res
        
    
if __name__ == "__main__":
    print(Solution().mono_decreasing_stack([30,38,30,36,35,40,28])) # [1,4,1,2,1,0,0]