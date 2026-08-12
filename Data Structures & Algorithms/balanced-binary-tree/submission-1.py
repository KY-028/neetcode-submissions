# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balanced = True
        def dfs(node):
            nonlocal balanced
            if not node:
                return 0

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            
            if abs(right-left) > 1:
                balanced = False
            return max(left, right)
        dfs(root)

        return balanced
