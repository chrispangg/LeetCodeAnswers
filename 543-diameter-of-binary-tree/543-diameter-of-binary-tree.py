# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root):
            if not root:
                # the height of an empty node is -1
                # not 0 because 0 is not a single node
                return -1
            
            # print(str(root.val))
            left, right = dfs(root.left), dfs(root.right)
            
            # 2 + left + right finds the diameter
            # if diameter is larger than than height
            res[0] = max(res[0], 2 + left + right)
            
            print(res[0])
            
            # the height is 
            return 1 + max(left, right)
        
        dfs(root)
        print(str(res))
        
        return res[0]
        
        
    