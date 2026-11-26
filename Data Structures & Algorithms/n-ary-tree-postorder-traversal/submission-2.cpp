/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> res;
        traverse(root, res);
        return res;
    }

private:
    void traverse(Node* r, vector<int>& res) {
        if (r == nullptr) return;

        for (Node* c : r->children) {
            traverse(c, res);
        }
        res.push_back(r->val);
    }
};