# 572. Subtree of Another Tree
# Solved
# Easy
# Topics
# Companies
# Hint
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True  # An empty tree is always a subtree
        if not root:
            return False  # Non-empty tree cannot be a subtree of an empty tree
        
        if self.isSameTree(root, subRoot):
            return True
        
        # Check the left and right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True  # Both trees are empty
        if not s or not t:
            return False  # One tree is empty and the other is not
        if s.val != t.val:
            return False  # Values of the nodes do not match
        
        # Recursively check the left and right subtree
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
