# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Find mid point, then reverse everything from mid point to the end
merge two list back together
[1,2,3,4,5,6] -> [1,6,2,5,3,4]
1,2,3
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find mid
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse from slow to end
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge two lists together
        list1 = head
        list2 = prev
        while list1 and list2:
            temp = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp
            list1,list2 = temp, temp2
    
        return head
        

            
            
        
