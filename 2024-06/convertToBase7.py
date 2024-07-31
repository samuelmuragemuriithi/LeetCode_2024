# 504. Base 7
# Solved
# Easy
# Topics
# Companies
# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
 

# Constraints:

# -107 <= num <= 107


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Determine the sign and work with the absolute value of num
        negative = num < 0
        num = abs(num)
        
        # List to hold the digits of the base 7 representation
        base7_digits = []
        
        # Convert to base 7
        while num > 0:
            base7_digits.append(str(num % 7))
            num //= 7
        
        # Join the digits and add the negative sign if needed
        base7_str = ''.join(base7_digits[::-1])
        
        return "-" + base7_str if negative else base7_str
