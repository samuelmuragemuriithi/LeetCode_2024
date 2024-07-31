# 448. Find All Numbers Disappeared in an Array
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Iterate through the array
        for num in nums:
            # Get the index corresponding to the absolute value of num - 1
            index = abs(num) - 1
            # Mark the number at that index as negative if it's not already marked
            nums[index] = -abs(nums[index])
        
        # Now, iterate through the modified array and append the indices of positive values to the result
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result
