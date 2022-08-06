# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Merge Sort
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return
        elif len(lists) <= 1:
            return lists[0]
        
        curNode = dummy = ListNode(float('-inf'))
        
        for i in range(len(lists)):
            curNode = self.merge(curNode, lists[i])
            
        return dummy.next
    
    def merge(self, left, right):
        curNode = dummy = ListNode(float('-inf'))
        
        while left and right:
            
            if left.val > right.val:
                curNode.next = right
                right = right.next
            else:
                curNode.next = left
                left = left.next
                
            curNode = curNode.next
        
        
        curNode.next = left if left else right
        
        return dummy.next
                
    
    
        

    
