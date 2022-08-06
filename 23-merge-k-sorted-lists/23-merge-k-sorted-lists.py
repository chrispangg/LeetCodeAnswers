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
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            
            # increment by 2 as we are merging 2 lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
                
            lists = mergedLists
                
        return lists[0]
    
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
                
    
    
        

    
