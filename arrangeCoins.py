# 441. Arranging Coins
# Solved
# Easy
# Topics
# Companies
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# # 1 <= n <= 231 - 1

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            coins_needed = (mid * (mid + 1)) // 2
            if coins_needed == n:
                return mid
            elif coins_needed < n:
                left = mid + 1
            else:
                right = mid - 1
        return right  # Lower bound is the closest complete row

# Test cases
solution = Solution()
print(solution.arrangeCoins(5))  # Output: 2
print(solution.arrangeCoins(8))  # Output: 3
