# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node, minimum, maximum):
            if not node:
                return True

            if minimum < node.val < maximum:
                left = dfs(node.left, minimum, node.val)
                right = dfs(node.right, node.val, maximum)
                return left and right
            return False

        return dfs(root, float('-inf'), float('inf'))