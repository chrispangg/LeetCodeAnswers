# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prevNode = None
        currentNode = head
        
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
            
        
        return prevNode
            
        
        
        
"""
Solution:
keep track of the next node
point current node to the prev node
move currentNode pointer to the next node

"""