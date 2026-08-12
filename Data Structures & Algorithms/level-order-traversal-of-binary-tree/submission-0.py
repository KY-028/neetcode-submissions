# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        to_visit = collections.deque()
        to_visit.append(root)

        while to_visit:
            size = len(to_visit)
            level = []
            for i in range(size):
                # pop each and append all its children
                node = to_visit.popleft()
                if node:
                    level.append(node.val)
                    to_visit.append(node.left)
                    to_visit.append(node.right)
            if level:
                answer.append(level)
        return answer