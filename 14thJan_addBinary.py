# 67. Add Binary
# Solved
# Easy
# Topics
# Companies
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Make sure a is the longer string
        if len(a) < len(b):
            a, b = b, a

        result = []
        carry = 0

        # Iterate through the strings in reverse order
        i, j = len(a) - 1, len(b) - 1
        while i >= 0:
            # Sum the corresponding digits and the carry
            total = int(a[i]) + carry
            if j >= 0:
                total += int(b[j])
                j -= 1

            # Update carry and append the current digit to the result
            carry, digit = divmod(total, 2)
            result.append(str(digit))

            i -= 1

        # If there's still a carry, append it to the result
        if carry:
            result.append(str(carry))

        # Reverse the result and join to get the final binary string
        return ''.join(result[::-1])

        