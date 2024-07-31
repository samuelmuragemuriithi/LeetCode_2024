# 557. Reverse Words in a String III
# Solved
# Easy
# Topics
# Companies
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()
        
        # Reverse each word and store the result in a new list
        reversed_words = [word[::-1] for word in words]
        
        # Join the reversed words with a single space and return the result
        return ' '.join(reversed_words)

# Example usage
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))  # Output: "s'teL ekat edoCteeL tsetnoc"
print(solution.reverseWords("Mr Ding"))                      # Output: "rM gniD"
