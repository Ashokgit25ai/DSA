# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.



# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome(s):
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()

    # Initialize two pointers
    left = 0
    right = len(s) - 1

    # Traverse the string from both ends
    while left <= right:

        # Skip non-alphanumeric characters from the left side
        if not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from the right side
        elif not s[right].isalnum():
            right -= 1

        # If characters match, move both pointers inward
        elif s[left] == s[right]:
            left += 1
            right -= 1

        # Mismatch found, string is not a palindrome
        else:
            return False

    # All valid characters matched
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)  # Due to s.lower()




#### SPACE COMPLEXITY O(1) ####

def isPalindrome(s):
    # Convert string to lowercase for case-insensitive comparison

    # Initialize two pointers at both ends of the string
    left = 0
    right = len(s) - 1

    # Continue until pointers meet or cross
    while left <= right:

        # Skip non-alphanumeric characters from the left side
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from the right side
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters at both pointers
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False  # Mismatch found

    return True  # All valid characters matched

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))