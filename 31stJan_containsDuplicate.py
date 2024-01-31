# 217. Contains Duplicate
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique elements
        seen = set()
        
        # Iterate through the array
        for num in nums:
            # If the element is already in the set, return True (contains duplicate)
            if num in seen:
                return True
            # Otherwise, add the element to the set
            seen.add(num)
        
        # If no duplicates are found, return False
        return False
