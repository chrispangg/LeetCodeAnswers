# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = [[root.val]]
        
        stack = [root] if root else []
        while stack:
            queue = []
            for node in stack:
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
                
            values = [node.val for node in queue]
            res.append(values) if values else None
            
            stack = queue
                
        return res