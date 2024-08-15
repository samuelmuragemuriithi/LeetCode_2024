"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
 

Constraints:

1 <= n <= 231 - 1
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Perform XOR with right-shifted number
        xor = n ^ (n >> 1)
        # Check if xor + 1 is a power of 2 (all bits are 1)
        return (xor & (xor + 1)) == 0

# Example usage:
sol = Solution()
print(sol.hasAlternatingBits(5))  # Output: True
print(sol.hasAlternatingBits(7))  # Output: False
print(sol.hasAlternatingBits(11)) # Output: False


        
