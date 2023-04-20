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
unsigned long long max_len = 0;
unordered_map<unsigned long long, unsigned long long> map;
void dfs(TreeNode* node, unsigned long long depth, unsigned long long col_index) {
  if (node == nullptr) {
    return;
  }
  if (map.find(depth) == map.end()) {
    map[depth] = col_index;
  }
  max_len = max(max_len, col_index - map[depth] + 1);
  dfs(node->left, depth + 1, 2 * col_index);
  dfs(node->right, depth + 1, 2 * col_index + 1);
} 
public:
    int widthOfBinaryTree(TreeNode* root) {
      dfs(root, 0, 0);
      return max_len;
    }
};
