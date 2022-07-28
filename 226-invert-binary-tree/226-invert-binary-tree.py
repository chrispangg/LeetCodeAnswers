# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        
        while queue:
            node = queue.pop()
            
            if node:
                temp = node.right
                node.right = node.left
                node.left = temp
                
                queue.append(node.left)
                queue.append(node.right)
        
        return root

        
"""
Solution: BFS, iterative approach
With BFS, we need to have a queue for storing the nodes
As we 
"""