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
    vector<double> averageOfLevels(TreeNode* root) {
        std::vector<double> output;
        std::deque<TreeNode*> dq{root};
        while (!dq.empty()) {
            int size = dq.size();
            double acc = 0.0;
            for (int i = 0; i < size; ++i) {
                acc += dq.front()->val;
                TreeNode* node = dq.front();
                dq.pop_front();
                if (node->left) {
                    dq.push_back(node->left);
                }
                if (node->right) {
                    dq.push_back(node->right);
                }
            }
            output.push_back(acc / (double) size);
        }
        return output;
    }
};
