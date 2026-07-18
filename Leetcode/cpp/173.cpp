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
class BSTIterator {
public:
    std::vector<int> values;
    int cur = -1;

    BSTIterator(TreeNode* root) {
        values.clear();
        std::function<void(TreeNode*)> generator = [&](TreeNode* node) -> void {
            if (node != nullptr) {
                generator(node->left);
                values.push_back(node->val);
                generator(node->right);
            }
            return;
        };
        generator(root);
        cur = 0;
    }
    
    int next() {
        if (cur < values.size()) {
            return values[cur++];
        }
        return -1;
    }
    
    bool hasNext() {
        return cur < values.size();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
