# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(node):
            if not node:
                return
            if node.left and node.right:
                temp = node.right
                node.right = node.left
                node.left = temp
                dfs(node.left)
                dfs(node.right)
            elif node.left:
                node.right = node.left
                node.left = None
                dfs(node.right)
            elif node.right:
                node.left = node.right
                node.right = None
                dfs(node.left)
        dfs(root)
        return root
            