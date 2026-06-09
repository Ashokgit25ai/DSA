
def findDisappearedNumbers(nums):
    """
    LeetCode 448 - Find All Numbers Disappeared in an Array

    Question:
    Given an array nums of n integers where nums[i] is in the range [1, n],
    return an array of all the integers in the range [1, n] that do not
    appear in nums.

    Approach:
    1. Use the input array itself to mark visited numbers.
    2. For each number, use its value as an index.
    3. Mark the corresponding index as negative.
    4. After marking, positive values indicate missing numbers.
    5. Collect and return the missing numbers.

    Time Complexity: O(n)
    Space Complexity: O(1) (excluding output array)
    """

    # Mark visited numbers
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])

    # Collect missing numbers
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)

    return result
nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))