# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:               
        res = [0]
        
        def dfs(root):
            if not root:
                return -1
            
            left, right = dfs(root.left), dfs(root.right)
            
            diff = abs(left - right)
            
            res[0] = max(res[0], diff)
        
            return 1 + max(left, right)
        
        dfs(root)
        if res[0] > 1:
            return False            
        
        return True