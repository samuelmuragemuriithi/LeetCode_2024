"""
671. Second Minimum Node In a Binary Tree
Solved
Easy
Topics
Companies
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

 

 

Example 1:


Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:


Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
 

Constraints:

The number of nodes in the tree is in the range [1, 25].
1 <= Node.val <= 231 - 1
root.val == min(root.left.val, root.right.val) for each internal node of the tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        # Using a set to store unique values
        unique_values = set()

        def dfs(node):
            if node:
                unique_values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        # Perform DFS to collect all unique values
        dfs(root)

        # If there are less than 2 unique values, return -1
        if len(unique_values) < 2:
            return -1

        # Convert set to list and sort to find the second minimum
        unique_values = sorted(unique_values)
        return unique_values[1]

# Example usage:
# root1 = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
# print(Solution().findSecondMinimumValue(root1))  # Output: 5

# root2 = TreeNode(2, TreeNode(2), TreeNode(2))
# print(Solution().findSecondMinimumValue(root2))  # Output: -1
