# 409. Longest Palindrome
# Solved
# Easy
# Topics
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Initialize a hashmap to store the frequency of each letter
        letter_count = {}
        
        # Count the frequency of each letter
        for letter in s:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        # Initialize variables to keep track of the length of the longest palindrome
        length = 0
        odd_count = 0
        
        # Iterate through the letter counts
        for count in letter_count.values():
            # Add the even count of letters to the length of the palindrome
            length += count // 2 * 2
            # If the count is odd, mark it
            if count % 2 != 0:
                odd_count = 1
        
        # If there are odd counts, add one to the length of the palindrome
        length += odd_count
        
        return length

# Test cases
solution = Solution()
print(solution.longestPalindrome("abccccdd"))  # Output: 7
print(solution.longestPalindrome("a"))          # Output: 1

        