class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))  # [1,2]
    print(s.twoSum([2,3,4], 6))  # [1,3]
    print(s.twoSum([-1,0], -1))  # [1,2]