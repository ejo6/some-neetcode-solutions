# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            post = cur.next    # store next node
            cur.next = prev    # reverse link
            prev = cur         # move prev forward
            cur = post         # move cur forward

        return prev