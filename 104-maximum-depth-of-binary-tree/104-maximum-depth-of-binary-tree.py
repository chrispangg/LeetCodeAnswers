# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [root] if root else []
        
        while stack:
            res += 1
            queue = []
            for node in stack:
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
            
            stack = queue
        
        return res
        
        
            