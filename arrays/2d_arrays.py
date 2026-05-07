# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

def find_num(arr,target):
    left = 0
    right = ((len(arr) * len(arr[0]))-1)
    mid = (left + right) // 2
    
    while left <= right:
        row = mid // right
        col = mid % right
        mid_val = arr[row][col]
        if mid_val == target:
            return True
        elif mid_val < target:
            right = mid-1
        else:
            left = mid+1        
    return False

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(find_num(arr,target))