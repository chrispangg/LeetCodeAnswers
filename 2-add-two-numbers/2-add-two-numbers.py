# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1, arr2 = [],[]
        
        while l1:
            arr1.append(l1.val)
            l1 = l1.next
        
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
        
        num1 = 0
        for i in range(len(arr1)):
            multiplier = 10**i
            num1 += arr1[i] * multiplier        
        
        num2 = 0
        for i in range(len(arr2)):
            multiplier = 10**i
            num2 += arr2[i] * multiplier  
        
        total = num1 + num2
        arrT = [int(a) for a in str(total)]
        arrT.reverse()
        print(arrT)
        
        prevNode = None
        while arrT:
            currNode = ListNode(arrT.pop(), prevNode)
            prevNode = currNode
        
        return currNode
