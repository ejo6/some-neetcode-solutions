# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        length = 0

        while head is not None:
            length += 1
            head = head.next

        if length == 1: return None
        nthIndex = length - n

        if nthIndex == 0: return dummy.next

        head = dummy
        i = 0

        while i < nthIndex - 1:
            head = head.next
            i += 1
        
        head.next = head.next.next

        return dummy
