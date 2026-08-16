# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        res = root.val

        def dfs(node):
            nonlocal counter, res
            if not node:
                return 
            # in order traversal
            dfs(node.left)
            if counter == 0: # if an answer has been found
                return
            
            counter -= 1
            # if this is exactly the node we've found the solution
            if counter == 0:
                res = node.val
                return
            dfs(node.right) # only if counter still > 0 do we go right
        
        dfs(root)
        return res