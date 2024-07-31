# 14. Longest Common Prefix
# Easy
# 16.7K
# 4.4K
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        reference_str = strs[0]

        for i in range(len(reference_str)):
            char = reference_str[i]

            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return reference_str[:i]

        return reference_str

# Example usage:
sol = Solution()

strs1 = ["flower", "flow", "flight"]
print(sol.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(sol.longestCommonPrefix(strs2))  # Output: ""

        