# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize a pointer to keep track of the position to place the next non-zero element
        insert_pos = 0
        
        # Iterate through the array
        for num in nums:
            # If the current element is non-zero
            if num != 0:
                # Move the non-zero element to the position indicated by insert_pos
                nums[insert_pos] = num
                # Move insert_pos to the next position
                insert_pos += 1
        
        # After placing all non-zero elements, fill the rest of the array with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0