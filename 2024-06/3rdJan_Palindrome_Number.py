# 9. Palindrome Number
# Easy
# 11.8K
# 2.7K
# Companies
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        str_x = str(x)
        
        # Compare the string with its reverse
        return str_x == str_x[::-1]

# Examples
sol = Solution()
print(sol.isPalindrome(121))    # Output: True
print(sol.isPalindrome(-121))   # Output: False
print(sol.isPalindrome(10))     # Output: False
