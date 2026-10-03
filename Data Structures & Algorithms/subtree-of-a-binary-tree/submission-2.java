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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null) return true;
        if (root == null) return false;

        if (compareTrees(root, subRoot)) return true;
        else {
            return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
        }
    }

    public boolean compareTrees(TreeNode r, TreeNode sr) {
        if (r == null && sr == null) return true;
        if (r == null || sr == null) return false;
        if (r.val != sr.val) return false;
        return compareTrees(r.left, sr.left) && compareTrees(r.right, sr.right);
    }
}
