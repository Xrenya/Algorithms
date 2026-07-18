/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (root == nullptr) {
            return root;
        }
        std::vector<Node*> stack;
        stack = {root};
        while (!stack.empty()) {
            int size = stack.size();
            std::vector<Node*> newStack;
            Node* prev = nullptr;
            for (int i = 0; i < size; ++ i) {
                Node* node = stack.back();
                stack.pop_back();
                node->next = prev;
                prev = node;
                if (node->right != nullptr) {
                    newStack.push_back(node->right);
                }
                if (node->left != nullptr) {
                    newStack.push_back(node->left);
                }
            }
            std::reverse(newStack.begin(), newStack.end());
            stack = newStack;
        }
        return root;
    }
    Node* connectDeque(Node* root) {
        if (root == nullptr) {
            return root;
        }
        std::deque<Node*> stack;
        stack.push_back(root);
        while (!stack.empty()) {
            int size = stack.size();
            Node* prev = nullptr;
            for (int i = 0; i < size; ++ i) {
                Node* node = stack.front();
                stack.pop_front();
                node->next = prev;
                prev = node;
                if (node->right != nullptr) {
                    stack.push_back(node->right);
                }
                if (node->left != nullptr) {
                    stack.push_back(node->left);
                }
            }
        }
        return root;
    }
};
