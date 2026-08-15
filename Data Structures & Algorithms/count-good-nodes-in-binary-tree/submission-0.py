# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maximum):
            if not node:
                return 0

            temp_sum = 0
            if node.val >= maximum:
                temp_sum += 1
            maximum = max(maximum, node.val)
            temp_sum += dfs(node.left, maximum)
            temp_sum += dfs(node.right, maximum)
            return temp_sum

        return dfs(root, float('-inf'))