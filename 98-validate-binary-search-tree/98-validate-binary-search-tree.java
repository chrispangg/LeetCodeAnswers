/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        //DFS in order, if the value is less than the previous value, we know it's wrong
        ArrayList<Integer> list = new ArrayList<Integer>();
        ArrayList<Integer> result = dfsInorderTraverse(root, list);
        boolean status = true;
        for(int i = 1; i < result.size(); i++){
            if(result.get(i-1) >= result.get(i)){
                status = false;
                break;
            }
        }
        return status;
    }
    
    public ArrayList<Integer> dfsInorderTraverse(TreeNode node, ArrayList<Integer> list){
        //base case: return list if node == null;
        if(node == null){
            return list;
        }
        
        //DFS Inorder -> Left -> Node -> Right
        if(node.left != null){
            dfsInorderTraverse(node.left, list);
        }
        
        list.add(node.val);
        
        if(node.right != null){
            dfsInorderTraverse(node.right, list);
        }
        
        return list;
    }
}