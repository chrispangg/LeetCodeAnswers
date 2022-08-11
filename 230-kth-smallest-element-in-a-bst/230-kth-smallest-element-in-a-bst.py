# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        curr = root
        count = 0
        while curr or stack:
            # while loop will append all the left nodes 
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # if curr is None (leaf node), we gone too far, so we pop from stack
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right
        
        return -1