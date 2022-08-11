# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Example: preorder = [3,9,20,15,7], Inorder = [9,3,15,20,7]

root.left 1st level:
    preorder[1:mid + 1] -> [9]
    inorder[:mid] -> [9]

root.right 1st level:
    preorder[mid + 1:] -> [20,15,7]
    inorder[mid + 1:] -> [15,20,7]
        
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid  = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root
        
        