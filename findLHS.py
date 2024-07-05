# 594. Longest Harmonious Subsequence
# Solved
# Easy
# Topics
# Companies
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 2
# Example 3:

# Input: nums = [1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109


from collections import defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Create a dictionary to store the frequency of each number
        freq = defaultdict(int)
        
        # Populate the frequency dictionary
        for num in nums:
            freq[num] += 1
        
        # Initialize the maximum length of the harmonious subsequence
        max_length = 0
        
        # Iterate through the keys in the frequency dictionary
        for num in freq:
            # Check if the consecutive number exists in the dictionary
            if num + 1 in freq:
                # Update the maximum length if a longer subsequence is found
                max_length = max(max_length, freq[num] + freq[num + 1])
        
        return max_length
