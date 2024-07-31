# 144. Binary Tree Preorder Traversal
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        while root or stack:
            if root:
                result.append(root.val)
                if root.right:
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()

        return result

# Example usage:
# Create a binary tree [1, null, 2, 3]
#     1
#      \
#       2
#      /
#     3
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
solution = Solution()
print(solution.preorderTraversal(root))  # Output: [1, 2, 3]
