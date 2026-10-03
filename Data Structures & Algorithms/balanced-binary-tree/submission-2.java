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
    private boolean balanced = true;

    public boolean isBalanced(TreeNode root) {
        depth(root);
        return balanced;
    }

    public int depth(TreeNode root) {
        if (!balanced) return 0; // short circuit
        if (root == null) return 0;

        int leftHeight = depth(root.left);
        int rightHeight = depth(root.right);

        int diff = leftHeight - rightHeight;
        if (diff < -1 || diff > 1) {balanced = false; return 0;}

        return Math.max(leftHeight, rightHeight) + 1;
    }   
}
