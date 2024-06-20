# 541. Reverse String II
# Solved
# Easy
# Topics
# Companies
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert the string to a list of characters to make modifications easier
        s = list(s)
        
        # Iterate over the string in steps of 2k
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters in the current 2k chunk
            s[i:i+k] = reversed(s[i:i+k])
        
        # Convert the list of characters back to a string and return it
        return ''.join(s)
