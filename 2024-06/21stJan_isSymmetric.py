# 101. Symmetric Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
 

# Follow up: Could you solve it both recursively and iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            # Base case: if both nodes are None, they are mirrors
            if not left and not right:
                return True
            # If one of the nodes is None and the other is not, they are not mirrors
            if not left or not right:
                return False
            # Check if values are equal and if subtrees are mirrors of each other
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        # Check if the tree is symmetric starting from the root
        return isMirror(root, root)
