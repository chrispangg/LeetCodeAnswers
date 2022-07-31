# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Shift fast pointer forward to the correct position
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Shift both pointers until the fast pointer reaches the end
        while right:
            left = left.next
            right = right.next
        
        # Delete
        left.next = left.next.next
        
        return dummy.next