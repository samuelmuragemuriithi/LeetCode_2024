# 222. Count Complete Tree Nodes
# Solved
# Easy
# Topics
# Companies
# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.height(root.left)

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if left_height == right_height:
            # Left subtree is perfect and right subtree is complete
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Left subtree is complete and right subtree is perfect
            return (1 << right_height) + self.countNodes(root.left)

# Test cases
# Example 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

sol = Solution()
print(sol.countNodes(root))  # Output: 6

# Example 2
root = None
print(sol.countNodes(root))  # Output: 0

# Example 3
root = TreeNode(1)
print(sol.countNodes(root))  # Output: 1
