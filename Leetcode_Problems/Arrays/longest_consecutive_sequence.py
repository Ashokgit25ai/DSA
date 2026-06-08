# 128. Longest Consecutive Sequence
#
# Approach: Hash Set
#
# Idea:
# - Store all numbers in a set for O(1) lookups.
# - A number is considered the start of a sequence if
#   its previous number (num - 1) does not exist in the set.
# - Once a sequence start is found, keep checking the next
#   consecutive numbers and count the sequence length.
# - Track the maximum sequence length encountered.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

def longestConsecutive(self, nums):
    count = 0
    maximum_length = 0

    # Convert list to set for fast lookups
    set_nums = set(nums)

    # Iterate through unique numbers
    for num in set_nums:

        # Check if current number is the start of a sequence
        if num - 1 not in set_nums:

            # Count consecutive numbers
            while num in set_nums:
                count += 1
                num += 1

            # Update longest sequence length
            maximum_length = max(maximum_length, count)

            # Reset count for the next sequence
            count = 0

    return maximum_length

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))