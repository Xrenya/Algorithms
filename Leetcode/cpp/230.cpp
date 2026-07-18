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
    int kthSmallest(TreeNode* root, int k) {
        int value = -1;
        std::function<void(TreeNode*)> dfs = [&](TreeNode* node) -> void {
             if (node) {
                dfs(node->left);
                --k;
                if (k == 0){
                    value = node->val;
                }
                dfs(node->right);

             }
        };
        dfs(root);
        return value;
    }
};
