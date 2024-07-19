# 628. Maximum Product of Three Numbers
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        # Consider the two possible maximum products
        max_product_1 = nums[-1] * nums[-2] * nums[-3]
        max_product_2 = nums[0] * nums[1] * nums[-1]
        
        # Return the maximum of the two
        return max(max_product_1, max_product_2)

# Test cases
solution = Solution()

print(solution.maximumProduct([1, 2, 3]))     # Output: 6
print(solution.maximumProduct([1, 2, 3, 4]))  # Output: 24
print(solution.maximumProduct([-1, -2, -3]))  # Output: -6
