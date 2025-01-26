def threeSumClosest(nums, target):
    nums.sort()  # Sort the array to use the two-pointer approach
    closest_sum = float('inf')  # Initialize with an infinitely large value

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1  # Two pointers

        while left < right:
            # Calculate the current sum of the three numbers
            current_sum = nums[i] + nums[left] + nums[right]

            # If the current sum is closer to the target, update the closest sum
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            # Move the pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum  # If exactly equal to the target, return the sum

    return closest_sum

# Example usage:
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print("The sum closest to the target is:", result)
