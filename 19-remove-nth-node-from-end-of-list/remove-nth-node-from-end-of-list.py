# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        left = head

        # Move right pointer n elements away from the left pointer.
        for i in range(n):
            right = right.next
    
        # Removal of the head node.
        if not right:
            return head.next
    
        # Move both pointers until right pointer reaches the last node.
        while right.next:
            right = right.next
            left = left.next

        # At this point, left pointer points to (n-1)th element.
        # So link it to next to next element of left.
        left.next = left.next.next

        return head
        