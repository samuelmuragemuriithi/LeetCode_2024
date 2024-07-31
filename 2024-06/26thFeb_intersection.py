# 349. Intersection of Two Arrays
# Solved
# Easy
# Topics
# Companies
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000



from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert the arrays to sets
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection of the two sets
        intersect = set1.intersection(set2)
        
        # Convert the intersection set back to a list
        return list(intersect)

# Test cases
solution = Solution()

nums1_1 = [1, 2, 2, 1]
nums2_1 = [2, 2]
print(solution.intersection(nums1_1, nums2_1))  # Output: [2]

nums1_2 = [4, 9, 5]
nums2_2 = [9, 4, 9, 8, 4]
print(solution.intersection(nums1_2, nums2_2))  # Output: [9, 4]


