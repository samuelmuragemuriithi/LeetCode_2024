# 326. Power of Three
# Solved
# Easy
# Topics
# Companies
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?



class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        # We can find the maximum power of 3 within the given range of integers
        max_power_of_three = 3 ** int((log(2**31 - 1) / log(3)))
        # If the number is divisible by the maximum power of three, it's a power of three
        return max_power_of_three % n == 0