"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
Build a dic from the original where key=originaln_ode, val=new_node
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copiedNodes = {None:None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            copiedNodes[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copiedNodes[curr]
            copiedNodes[curr].next = copiedNodes[curr.next]
            copiedNodes[curr].random = copiedNodes[curr.random]
            curr = curr.next
            
        return copiedNodes[head]
            
            
            
        
        
        