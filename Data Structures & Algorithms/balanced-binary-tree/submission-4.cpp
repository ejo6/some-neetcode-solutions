/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return (height(root) != -1);
    }

private:
    int height(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int leftDepth = height(root->left);
        if (leftDepth == -1) return -1;
        
        int rightDepth = height(root->right);
        if (rightDepth == -1) return -1;

        if (std::abs((rightDepth - leftDepth)) > 1) return -1;
        else {return (std::max(rightDepth, leftDepth) + 1);}
    }
};
