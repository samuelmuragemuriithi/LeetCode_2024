# 645. Set Mismatch
# Solved
# Easy
# Topics
# Companies
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = sum(nums)
        actual_square_sum = sum(x * x for x in nums)
        
        expected_sum = n * (n + 1) // 2
        expected_square_sum = n * (n + 1) * (2 * n + 1) // 6
        
        sum_diff = expected_sum - actual_sum
        square_sum_diff = expected_square_sum - actual_square_sum
        
        missing = (sum_diff + square_sum_diff // sum_diff) // 2
        duplicate = missing - sum_diff
        
        return [duplicate, missing]
