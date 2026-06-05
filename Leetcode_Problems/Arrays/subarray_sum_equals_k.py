# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Input: nums = [1,1,1], k = 2
# Output: 2

def subarraySum(nums, k):
        # Stores the final answer
        count = 0

        # Running prefix sum
        prefix_sum = 0

        # HashMap: {prefix_sum : frequency}
        # We start with {0:1} because before processing any element
        # the prefix sum is 0 and it has occurred once.
        prefix_map = {0: 1}

        # Traverse the array
        for num in nums:

            # Update running prefix sum
            prefix_sum += num

            # We need a previous prefix sum such that:
            # current_prefix - previous_prefix = k
            #
            # Therefore:
            # previous_prefix = current_prefix - k
            needed = prefix_sum - k

            # If we've seen 'needed' before,
            # then we found one or more valid subarrays
            if needed in prefix_map:

                # Add the number of times that prefix sum appeared
                count += prefix_map[needed]

            # Store/update the current prefix sum frequency
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] += 1
            else:
                prefix_map[prefix_sum] = 1

        return count
nums = [1,1,1]
k = 2
print(subarraySum(nums,k))