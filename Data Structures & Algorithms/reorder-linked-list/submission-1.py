# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get midpoint in one pass
        slow = head
        fast = head.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None

        # Reverse second half
        second_head = self.reverseList(second_head)

        # Merge the two halves
        dummy = head

        while (second_head is not None):
            temp_next_head = head.next
            temp_next_second_head = second_head.next
            head.next = second_head
            second_head.next = temp_next_head

            head = temp_next_head
            second_head = temp_next_second_head


    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return None

        prev = None
        curr = head
        next = curr.next

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
        