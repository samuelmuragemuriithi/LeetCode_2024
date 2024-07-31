# 501. Find Mode in Binary Search Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
 

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # First pass to find the maximum frequency
        def inorder_traversal(node):
            nonlocal current_val, current_count, max_count
            if not node:
                return
            
            inorder_traversal(node.left)
            
            if node.val == current_val:
                current_count += 1
            else:
                current_val = node.val
                current_count = 1
            
            if current_count > max_count:
                max_count = current_count
            
            inorder_traversal(node.right)
        
        current_val = None
        current_count = 0
        max_count = 0
        inorder_traversal(root)
        
        # Second pass to collect all the modes
        def collect_modes(node):
            nonlocal current_val, current_count, max_count, modes
            if not node:
                return
            
            collect_modes(node.left)
            
            if node.val == current_val:
                current_count += 1
            else:
                current_val = node.val
                current_count = 1
            
            if current_count == max_count:
                modes.append(node.val)
            
            collect_modes(node.right)
        
        current_val = None
        current_count = 0
        modes = []
        collect_modes(root)
        
        return modes
