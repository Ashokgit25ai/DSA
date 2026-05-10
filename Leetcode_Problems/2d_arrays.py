# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

def find_num(arr,target):
    rows = len(arr)
    cols = len(arr[0])
    left = 0
    right = ((rows * cols)-1)
    
    
    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        mid_val = arr[row][col]
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid+1
        else:
            right = mid-1        
    return False

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(find_num(arr,target))