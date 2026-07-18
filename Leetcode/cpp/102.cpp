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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        std::vector<std::vector<int>> output;
        std::deque<TreeNode*> dq{root};
        while (!dq.empty()) {
            int size = dq.size();
            std::vector<int> tmp;
            for (int i = 0; i < size; ++i) {
                TreeNode* node = dq.front();
                dq.pop_front();
                tmp.push_back(node->val);
                if (node->left) {
                    dq.push_back(node->left);
                }
                if (node->right) {
                    dq.push_back(node->right);
                }
            }
            output.push_back(tmp);
        }
        return output;
    }
};
