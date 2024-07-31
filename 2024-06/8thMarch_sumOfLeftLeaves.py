# 404. Sum of Left Leaves
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:

# Input: root = [1]
# Output: 0
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:
                if is_left:
                    return node.val
                else:
                    return 0
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)

# Test cases
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

sol = Solution()
print(sol.sumOfLeftLeaves(root1))  # Output: 24

root2 = TreeNode(1)
print(sol.sumOfLeftLeaves(root2))  # Output: 0
