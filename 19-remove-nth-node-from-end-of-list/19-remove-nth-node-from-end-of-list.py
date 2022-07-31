# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the list
        length = 0
        currNode = head
        while currNode.next:
            length += 1
            currNode = currNode.next
            
        currNode = head
        
        print(str(length))
        pos = length - n
        print(str(pos))
        
        #edge case when pos is 0
        if pos == -1:
            return head.next
        else:
        # loop forward to remove node
            for i in range(length):
                if i == pos:
                    tbrNode = currNode.next
                    currNode.next = currNode.next.next                
                    break;

                currNode = currNode.next
        
        return head