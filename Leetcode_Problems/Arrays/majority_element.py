# 169. Majority Element
#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Input: nums = [3,2,3]
# Output: 3

### BRUTE FORCE WITH TIME COMPLEXTY 0(n) AND SPACE COMPLEXITY O(n)  ###

# def majorityElement(nums):
#     length = len(nums)
#     major_value = length//2
#     store_values = {}

#     for ele in nums:
#         store_values[ele] = store_values.get(ele,0)+1

#     for key in store_values:
#         if store_values[key] > major_value:
#             return key
            
# nums = [3,2,3]
# print(majorityElement(nums))  


### BY USING BOYER'S MOORE VOTING ALGORITHM ###


def majorityElementByBoyersMooreVotingAlgo(nums):
    
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1
            
    return candidate


nums = [3,2,3]
print(majorityElementByBoyersMooreVotingAlgo(nums))
