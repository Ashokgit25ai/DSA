#238. Product of Array Except Self

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


def Product_of_Array_Except_Self(nums):
    length = len(nums)
    #create n length of array 
    answer = [1] * length
    
    #Set prefix to 1 to update the prefix value
    prefix = 1
    for pre_ele in range(length):
        #Add prefix to the answer Array based on answer index
        answer[pre_ele] = prefix
        #Update the prefix value
        prefix *= nums[pre_ele]
        
    suffix = 1
    #Traverse array from the end
    for suff_ele in range(length-1,-1,-1):
        #Multiply the suffix with the prefix in answer array based on answer index
        answer[suff_ele] *= suffix
        #Updste suffix value
        suffix *= nums[suff_ele]
         
         
    return answer

nums = [1,2,3,4]
print(Product_of_Array_Except_Self(nums))
        
