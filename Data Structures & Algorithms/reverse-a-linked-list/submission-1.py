# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        prev = None
        next = None

        while cur != None:
            next = cur.next
            cur.next = prev # update to before
            prev = cur # move node
            cur = next # move node

        return prev # last processed node! node = temp = null
