# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

# 977. Squares of a Sorted Array
#
# Approach-1: Two Pointers (Using max() and abs())
#
# Idea:
# - The largest square will always come from either the leftmost
#   negative number or the rightmost positive number.
# - Compare their absolute values using max().
# - Place the larger square at the end of the result array.
# - Move the corresponding pointer and continue.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

def sortedSquares(nums):
    left = 0
    right = len(nums) - 1

    # Result array
    new_arr = [0] * len(nums)

    # Fill result from right to left
    fill = len(new_arr) - 1

    while left <= right:

        # Find the larger absolute value
        max_value = max(abs(nums[left]), abs(nums[right]))

        # Store its square
        new_arr[fill] = max_value * max_value

        # Move the pointer that contributed the larger value
        if abs(nums[left]) == max_value:
            left += 1
        else:
            right -= 1

        fill -= 1

    return new_arr

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))





# Approach-2: Two Pointers (Direct Comparison - Optimized)
#
# Idea:
# - Compare absolute values at both ends directly.
# - Square the larger value and place it at the end
#   of the result array.
# - Move the corresponding pointer.
# - Continue until all positions are filled.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

def sortedSquares(nums):
    left = 0
    right = len(nums) - 1

    # Result array
    new_arr = [0] * len(nums)

    # Fill result from right to left
    fill = len(new_arr) - 1

    while left <= right:

        # Compare absolute values directly
        if abs(nums[left]) > abs(nums[right]):

            # Left side has larger magnitude
            new_arr[fill] = nums[left] * nums[left]
            left += 1

        else:

            # Right side has larger magnitude
            new_arr[fill] = nums[right] * nums[right]
            right -= 1

        fill -= 1

    return new_arr

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))
