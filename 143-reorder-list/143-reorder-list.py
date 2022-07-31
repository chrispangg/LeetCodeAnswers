# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use slow fast pointers to find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split the list and make the last node of the first list points to null
        second = slow.next
        prev = slow.next = None
        
        # reverse the second list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge two halfs
        first, second = head, prev
        while second: #use second becuase it may be a shorter list
            temp1, temp2 = first.next, second.next 
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
             
        