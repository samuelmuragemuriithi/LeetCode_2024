"""
680. Valid Palindrome II
Easy
Topics
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(i, j):
            """Helper function to check if a substring s[i:j+1] is a palindrome."""
            return all(s[k] == s[j-k+i] for k in range(i, j))
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Check the two possibilities: removing one character from either end
                return is_palindrome_range(left+1, right) or is_palindrome_range(left, right-1)
            left += 1
            right -= 1
        
        return True

        