# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


s = ["h", "e", "l", "l", "o"]

# Initialize two pointers:
# left starts from the beginning of the array
# right starts from the end of the array
left = 0
right = len(s) - 1

# Continue swapping until the pointers meet
while left < right:

    # Swap characters at left and right positions
    s[left], s[right] = s[right], s[left]

    # Move pointers toward the center
    left += 1
    right -= 1

# Print the reversed array
print(s)

# Time Complexity: O(n)
# - Each element is visited at most once.
#
# Space Complexity: O(1)
# - Reversal is done in-place without using extra space.
#
# Pattern Used: Two Pointers