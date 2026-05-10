# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
# Input -> x = 123
# Output -> 321

def reverse(x):
    
    rev = 0
    symbol = -1 if x<0 else 1
    x = abs(x)
    while x > 0:
        rem = x % 10
        # Check for overflow before updating res
        # If res > MAX_INT // 10, multiplying by 10 will overflow
        # If res == MAX_INT // 10, adding a digit > 7 will overflow
        if rev > (2**31-1)//10 or (rev == (2**31-1)//10 and rem > 7):
            return 0 
        rev = rev*10 + rem
        x = x//10
    
    return rev * symbol

x = 123
res = reverse(x)
print(res)