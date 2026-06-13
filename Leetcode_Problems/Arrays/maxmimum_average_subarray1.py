# LeetCode 643 - Maximum Average Subarray I
# Pattern: Fixed Size Sliding Window
#
# Problem:
# Given an integer array nums and an integer k,
# return the maximum average value of any contiguous subarray of length k.

def findMaxAverage(nums, k):
    # Calculate the sum of the first window of size k
    k_sum = sum(nums[:k])

    # Store the maximum window sum encountered so far
    max_sum = k_sum

    # Slide the window across the array
    for i in range(1, len(nums) - k + 1):

        # Remove the outgoing element and add the incoming element
        k_sum = k_sum - nums[i - 1] + nums[i + k - 1]

        # Update the maximum window sum if needed
        max_sum = max(max_sum, k_sum)

    # Return the maximum average
    return max_sum / (k * 1.0)


# Function Call
nums = [1, 12, -5, -6, 50, 3]
k = 4

result = findMaxAverage(nums, k)
print("Maximum Average:", result)


# Time Complexity: O(n)
# - Computing the first window sum takes O(k).
# - Sliding the window through the remaining elements takes O(n - k).
# - Overall complexity is O(n).

# Space Complexity: O(1)
# - Only a few variables (k_sum, max_sum, result) are used.
# - No extra data structures are created that depend on input size.

