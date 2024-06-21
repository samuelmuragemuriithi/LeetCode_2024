# 543. Diameter of Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Initialize the maximum diameter
        self.max_diameter = 0
        
        def height(node):
            if not node:
                return 0
            # Recursively find the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # The diameter through the current node is the sum of the heights of the left and right subtrees
            current_diameter = left_height + right_height
            
            # Update the maximum diameter
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)
        
        # Start the recursive height calculation
        height(root)
        
        return self.max_diameter

        