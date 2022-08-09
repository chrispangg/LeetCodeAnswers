# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BFS question. On each level, insert the right most value to our res array
return res array
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        stack= [root] if root else []
        
        while stack:
            queue = []
            for node in stack:
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
            
            
            value = queue[len(queue)-1].val if len(queue) - 1 >= 0 else None
            
            if value is not None:
                res.append(value)
            
            stack = queue
            
        print(res)
        return res
    