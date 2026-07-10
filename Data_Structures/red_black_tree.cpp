#include <iostream>
#include <queue>

enum Color { RED, BLACK };

template <typename T>
class Node {
public:
    T data;
    Color color = RED;
    Node<T>* left = nullptr;
    Node<T>* right = nullptr;
    Node<T>* parent = nullptr;
    
    Node(T data) : data(data) { }
};

template <typename T>
class RBTree {
private:
    Node<T>* root = nullptr;

    void rotate_left(Node<T>* x) {
        Node<T>* y = x->right;
        x->right = y->left;
        if (y->left != nullptr) y->left->parent = x;
        y->parent = x->parent;
        if (x->parent == nullptr) root = y;
        else if (x == x->parent->left) x->parent->left = y;
        else x->parent->right = y;
        y->left = x;
        x->parent = y;
    }

    void rotate_right(Node<T>* x) {
        Node<T>* y = x->left;
        x->left = y->right;
        if (y->right != nullptr) y->right->parent = x;
        y->parent = x->parent;
        if (x->parent == nullptr) root = y;
        else if (x == x->parent->right) x->parent->right = y;
        else x->parent->left = y;
        y->right = x;
        x->parent = y;
    }

    void fix_insert(Node<T>* k) {
        Node<T>* u;
        while (k->parent && k->parent->color == RED) {
            if (k->parent == k->parent->parent->right) {
                u = k->parent->parent->left;
                if (u && u->color == RED) {
                    u->color = BLACK;
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    k = k->parent->parent;
                } else {
                    if (k == k->parent->left) {
                        k = k->parent;
                        rotate_right(k);
                    }
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    rotate_left(k->parent->parent);
                }
            } else {
                u = k->parent->parent->right;
                if (u && u->color == RED) {
                    u->color = BLACK;
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    k = k->parent->parent;
                } else {
                    if (k == k->parent->right) {
                        k = k->parent;
                        rotate_left(k);
                    }
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    rotate_right(k->parent->parent);
                }
            }
            if (k == root) break;
        }
        root->color = BLACK;
    }

public:
    RBTree() = default;

    Node<T>* get_root() { return root; }

    void add(T data) {
        Node<T>* node = new Node<T>(data);
        Node<T>* y = nullptr;
        Node<T>* x = root;

        while (x != nullptr) {
            y = x;
            if (node->data < x->data) x = x->left;
            else if (node->data > x->data) x = x->right;
            else { delete node; return; }
        }

        node->parent = y;
        if (y == nullptr) root = node;
        else if (node->data < y->data) y->left = node;
        else y->right = node;

        fix_insert(node);
    }

    void pprint_levels() {
        if (root == nullptr) return;
        std::queue<Node<T>*> q;
        q.push(root);
        
        while (!q.empty()) {
            int lenLevel = q.size();
            for (int i = 0; i < lenLevel; ++i) {
                Node<T>* curr = q.front();
                q.pop();
                
                char c = (curr->color == RED) ? 'R' : 'B';
                std::cout << curr->data << "(" << c << ") ";
                
                if (curr->left) q.push(curr->left);
                if (curr->right) q.push(curr->right);
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    RBTree<int> tree;
    tree.add(5);
    tree.add(3);
    tree.add(6);
    tree.add(4);
    tree.add(2);
    
    std::cout << "Level print out [Node(Color)]:" << std::endl;
    tree.pprint_levels();
    
    return 0;
}
