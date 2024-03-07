
# Code
# Testcase
# Testcase
# Test Result
# 387. First Unique Character in a String
# Solved
# Easy
# Topics
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        
        # Count occurrences of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Find the index of the first unique character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        return -1
