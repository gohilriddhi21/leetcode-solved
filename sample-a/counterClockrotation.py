class Solution:
    # Rotate the array counter-clockwise by k steps
    
    # Time complexity: O(n)
    def rotateCounterClockwise(self, nums: list[int], k: int) -> list[int]:
        return nums[k-1:]+ nums[:k-1]
    
    def reverse_array(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
    def rotateCounterClockwise(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        k %= n
        
        self.reverse_array(nums, 0, k - 1)
        self.reverse_array(nums, k, n - 1)
        self.reverse_array(nums, 0, n - 1)
        return nums


if __name__ == '__main__':
    print(Solution().rotateCounterClockwise([1,2,3,4,5,6,7], 3)) 