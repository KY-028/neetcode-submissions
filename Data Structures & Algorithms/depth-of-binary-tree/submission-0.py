# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # dfs
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                return max(1 + left, 1 + right)
            else:
                return 0
        if not root:
            return 0
        
        return dfs(root)