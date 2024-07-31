# 383. Ransom Note
# Solved
# Easy
# Topics
# Companies
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of characters in both ransomNote and magazine
        ransomNote_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        # Iterate through each unique character in ransomNote
        for char, count in ransomNote_count.items():
            # If the character is not in the magazine or its count in magazine is less than in ransomNote, return False
            if char not in magazine_count or magazine_count[char] < count:
                return False
        
        # If all characters in ransomNote can be constructed from magazine, return True
        return True
