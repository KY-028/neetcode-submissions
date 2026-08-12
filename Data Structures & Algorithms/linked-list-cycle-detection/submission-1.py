# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointers
        # if cycle exists fast will always catch up with slow within n steps
        # this is because each iteration the gap between fast and slow - 1

        slow = head
        fast = head
        # edge case, no head or cycle of root node
        if not head:
            return False
        elif head.next == head:
            return True

        while True:
            if slow.next:
                slow = slow.next
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next

            if slow == fast:
                return True