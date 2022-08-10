# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, arr):
            if not node:
                return None
            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)
            return arr
        
        arr = dfs(root, [])
        print(arr)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True
        
            
            
            