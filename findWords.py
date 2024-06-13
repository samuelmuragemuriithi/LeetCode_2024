<!-- 500. Keyboard Row
Solved
Easy
Topics
Companies
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
 

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).  -->


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        Finds words that can be typed using letters from a single row of the American keyboard.

        Args:
            words: A list of strings representing words.

        Returns:
            A list of strings that can be typed using letters from a single row of the keyboard.
        """

        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        one_row_words = []

        for word in words:
            # Convert word to lowercase for case-insensitive check
            lowercase_word = word.lower()
            # Check if all characters belong to the same row
            if all(char in rows[0] for char in lowercase_word) or \
               all(char in rows[1] for char in lowercase_word) or \
               all(char in rows[2] for char in lowercase_word):
                one_row_words.append(word)

        return one_row_words

        