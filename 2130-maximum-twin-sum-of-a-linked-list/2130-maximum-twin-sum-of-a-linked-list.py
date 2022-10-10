# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        
        slow, fast = head, head
        while fast.next.next:
            res.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        res.append(slow.val)
        slow = slow.next
        i = -1
        maxVal = 0
        while slow:
            res[i] += slow.val
            maxVal = max(maxVal, res[i])
            
            i -= 1
            slow = slow.next
        
        return maxVal
        
        