# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        # dfs
        def dfs(node):
            nonlocal diameter
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                diameter = max(diameter, left + right)
                return 1 + max(left, right)
            else:
                return 0
        if not root:
            return 0
        dfs(root)
        return diameter