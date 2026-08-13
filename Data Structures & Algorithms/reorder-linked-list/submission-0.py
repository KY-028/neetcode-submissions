# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # first find the midpoint
        l = 0
        last = head
        while last:
            l += 1
            last = last.next

        mid = (l + 1) // 2
        node = head
        counter = 1
        while counter < mid:
            counter += 1
            node = node.next

        # split up second half
        temp = node.next # the beginning of the new list
        node.next = None # break up first half
        node = temp
        
        # now node is at mid, reverse second half
        prev = None
        while node:
            temp = node.next # store next node
            node.next = prev # make the current node point to prev
            prev = node # current node becomes prev
            node = temp      # next node becomes node
        
        # finally, update the list:
        list1 = head
        list2 = prev
        while list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2
