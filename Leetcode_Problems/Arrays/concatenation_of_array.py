# 1929. Concatenation of Array

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

def getConcatenation(nums):
        length = len(nums)
        answer = [0]*(2*length)

        for element in range(0,length):
            answer[element],answer[element+length] = nums[element],nums[element]
        return answer
    
nums = [1,2,1]
print(getConcatenation(nums))