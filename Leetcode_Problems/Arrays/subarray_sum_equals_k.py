# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Input: nums = [1,1,1], k = 2
# Output: 2

def subarraySum(nums, k):
        count = 0
        prefix_sum = 0
        store_value = {0:1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in store_value:
                count += store_value[prefix_sum - k]
            
            if prefix_sum in store_value:
                store_value[prefix_sum] += 1
            else:
                store_value[prefix_sum] = 1

        return count
nums = [1,1,1]
k = 2
print(subarraySum(nums,k))