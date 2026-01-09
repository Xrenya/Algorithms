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

#include <unordered_map>
#include <iostream>
#include <algorithm>


class Solution {
public:
    std::unordered_map<TreeNode*, int> map;

    void dfs(TreeNode* node, TreeNode* parent) {
        if (node) {
            map[node] = map[parent] + 1;
            dfs(node->left, node);
            dfs(node->right, node);
        }
    }

    TreeNode* answer(TreeNode* node, int max_depth) {
        if (!node || map[node] == max_depth) {
            return node;
        }
        TreeNode* left = answer(node->left, max_depth);
        TreeNode* right = answer(node->right, max_depth);
        return left && right ? node : (left ? left : right);
    }

    TreeNode* subtreeWithAllDeepest(TreeNode* root) {

        map[nullptr] = -1;
        dfs(root, nullptr);

        int max_depth = -1;
        for (const auto& [node, depth] : map) {
            max_depth = std::max(max_depth, depth);
        }

        return answer(root, max_depth);
    }
};
