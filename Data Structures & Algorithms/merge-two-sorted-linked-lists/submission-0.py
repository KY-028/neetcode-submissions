# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = list1
        cur2 = list2
        ans = None
        head = None

        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                if not head:
                    head = cur1
                    ans = head
                else:
                    head.next = cur1
                    head = head.next
                cur1 = cur1.next
            else:
                if not head:
                    head = cur2
                    ans = head
                else:
                    head.next = cur2
                    head = head.next
                cur2 = cur2.next

        # now add remaining 
        while cur1 is not None:
            if not head:
                head = cur1
                ans = head
            else:
                head.next = cur1
                head = head.next
            cur1 = cur1.next
        while cur2 is not None:
            if not head:
                head = cur2
                ans = head
            else:
                head.next = cur2
                head = head.next
            cur2 = cur2.next
        return ans


