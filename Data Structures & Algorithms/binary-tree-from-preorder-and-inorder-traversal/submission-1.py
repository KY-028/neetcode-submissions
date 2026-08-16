# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder): # finished building
                return None
            if inorder[inIdx] == limit: # this means we've reached the last item in the subtree
                inIdx += 1
                return None
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val) # the left tree is over until we reach this node's value
            root.right = dfs(limit) # the right tree is over until we reach the parent's value!
            return root
        
        return dfs(float('inf'))


        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])

        # Key: the index of the root in inorder gives us the subarray of its left/right subtrees
        # Also: the preordeer also has a partition of the left/right subtrees
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # preorder: starting from the next value, to the number of elements on the left
        # inorder: everything up till the position of that node (the left subtree)
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # preorder: starting from the right half, all the way till the end
        return root
        """
