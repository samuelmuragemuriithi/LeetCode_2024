# 463. Island Perimeter
# Solved
# Easy
# Topics
# Companies
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
 

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Add 4 for the current land cell
                    perimeter += 4

                    # If the cell above is also land, subtract 2 from the perimeter
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2

                    # If the cell to the left is also land, subtract 2 from the perimeter
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter

# Example usage:
solution = Solution()
grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid2 = [[1]]
grid3 = [[1,0]]

print(solution.islandPerimeter(grid1))  # Output: 16
print(solution.islandPerimeter(grid2))  # Output: 4
print(solution.islandPerimeter(grid3))  # Output: 4

        