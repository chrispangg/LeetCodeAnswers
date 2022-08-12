# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(node):
            if not node: return 0
            
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            
            # compute max path sum WITH split
            res[0] = max(res[0], node.val + leftMax + rightMax)
            
            return node.val + max(leftMax, rightMax) #return with no split
        
        dfs(root)
        return res[0]