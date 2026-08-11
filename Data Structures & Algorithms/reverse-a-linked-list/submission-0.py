# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        prev = None
        while node:
            temp = node.next # store the next node so we can continue traversing
            node.next = prev
            prev = node
            node = temp

        return prev # last processed node! node = temp = null
