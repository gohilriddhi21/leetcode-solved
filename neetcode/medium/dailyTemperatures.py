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

if __name__ == "__main__":
    print(Solution().dailyTemperatures([30,38,30,36,35,40,28])) # [1,4,1,2,1,0,0]