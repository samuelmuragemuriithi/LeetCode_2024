# 520. Detect Capital
# Solved
# Easy
# Topics
# Companies
# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1: All letters are capitals
        if word.isupper():
            return True
        
        # Case 2: All letters are not capitals
        if word.islower():
            return True
        
        # Case 3: Only the first letter is capital and the rest are lowercase
        if word[0].isupper() and word[1:].islower():
            return True
        
        # If none of the cases match, return False
        return False

        