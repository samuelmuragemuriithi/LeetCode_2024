# 605. Can Place Flowers
# Solved
# Easy
# Topics
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # To keep track of the number of flowers planted
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or out of bounds
                empty_previous = (i == 0) or (flowerbed[i - 1] == 0)
                empty_next = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if empty_previous and empty_next:
                    # Plant a flower here
                    flowerbed[i] = 1
                    count += 1
                    # If we have planted enough flowers, return true
                    if count >= n:
                        return True
        
        # If we couldn't plant enough flowers, return false
        return count >= n

# Example usage:
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1], 1))  # Output: True
print(solution.canPlaceFlowers([1,0,0,0,1], 2))  # Output: False
