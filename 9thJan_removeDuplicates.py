# 26. Remove Duplicates from Sorted Array
# Easy
# 13.5K
# 17.8K
# Companies
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize two pointers
        slow = 0

        # Iterate through the array
        for fast in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[fast] != nums[slow]:
                # Move the slow pointer and update the value
                slow += 1
                nums[slow] = nums[fast]

        # The unique elements are now in the first (slow + 1) positions
        # The remaining elements can be ignored

        return slow + 1  # Return the length of the unique elements

# Example usage:
solution = Solution()

nums1 = [1, 1, 2]
k1 = solution.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2, [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = solution.removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 2, 3, 4]

        