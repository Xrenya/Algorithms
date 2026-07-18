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
    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        std::vector<int> output;
        std::deque<TreeNode*> dq;
        dq.push_back(root);
        while (!dq.empty()) {
            int size = dq.size();
            int value = -1;
            for (int i = 0; i < size; ++i) {
                TreeNode* node = dq.front();
                value = dq.front()->val;
                dq.pop_front();
                if (node->left) {
                    dq.push_back(node->left);
                }
                if (node->right) {
                    dq.push_back(node->right);
                }
            }
            output.push_back(value);
        }
        return output;
    }
};
