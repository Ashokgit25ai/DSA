# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49



def maxArea(height):
    # Variable to store the maximum water found so far
    max_water = 0

    # Initialize two pointers at the beginning and end of the array
    left = 0
    right = len(height) - 1

    # Continue until the two pointers meet
    while left < right:

        # Width of the container is the distance between the two lines
        width = right - left

        # Height of the container is limited by the shorter line
        length = min(height[left], height[right])

        # Calculate the current water area
        water_quantity = width * length

        # Update the maximum water area if the current area is larger
        max_water = max(max_water, water_quantity)

        # Move the pointer pointing to the shorter line
        # to potentially find a taller line and increase the area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    # Return the maximum water area found
    return max_water

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))


# Pattern: Two Pointers + Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)