# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(node1, node2):
            if node1 and node2:
                if node1.val == node2.val:
                    return same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)
            elif node1 or node2:
                return False
            elif not node1 and not node2:
                return True
            return False

        ls = [root]
        while ls:
            node = ls.pop()
            if same_tree(node, subRoot):
                return True
            else:
                if node.left:
                    ls.append(node.left)
                if node.right:
                    ls.append(node.right)
        return False


        
            

        