# 205. Isomorphic Strings
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # If lengths are different, they can't be isomorphic
            return False
        
        char_map = {}  # Map to store character mappings
        
        for i in range(len(s)):
            if s[i] not in char_map:  # If the character is not mapped yet
                if t[i] in char_map.values():  # If the character is already mapped to another character
                    return False
                char_map[s[i]] = t[i]  # Map s[i] to t[i]
            else:
                if char_map[s[i]] != t[i]:  # If the mapping doesn't match
                    return False
        
        return True

# Example usage:
solution = Solution()
print(solution.isIsomorphic("egg", "add"))    # Output: True
print(solution.isIsomorphic("foo", "bar"))    # Output: False
print(solution.isIsomorphic("paper", "title"))# Output: True
