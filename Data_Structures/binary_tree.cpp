#include <iostream>
#include <queue>
#include <utility> 


template <typename T>
class Node {
public:
    T data;
    Node<T> * left = nullptr;
    Node<T> * right = nullptr;
    
    Node(T data) : data(data) { }
    Node(T data, Node<T> * left, Node<T> * right) : data(data), left(left), right(right) { }
    
    ~Node() { }
};

template <typename T>
class Tree {
public:
    Node<T> * root = nullptr;
    Tree() = default;
    Tree(Node<T> * node) {
        root = node;
    }
    
    std::pair<Node<T>*, Node<T>*> find(Node<T>* child, Node<T>* parent, T value) {
        if (child == nullptr || child->data == value) {
            return {child, parent};
        } else if (child->data < value) {
            return find(child->right, child, value);
        }
        return find(child->left, child, value);
    }
    
    void add(Node<T>* node) {
        if (root == nullptr) {
            root = node;
            return;
        }
        auto [child, parent] = find(root, nullptr, node->data);
        if (child != nullptr) {
            return;
        }
        if (node->data < parent->data) {
            parent->left = node;
        } else {
            parent->right = node;
        }
        
    }
    
    void delete_leaf(Node<T>* child, Node<T>* parent) {
        if (parent == nullptr){
            root = nullptr;
        } else if (parent->left == child) {
            parent->left = nullptr;
        } else {
            parent->right = nullptr;
        }
        delete child;
        return;
    }
    
    void delete_one_child(Node<T>* child, Node<T>* parent) {
        Node<T>* nextNode = (child->left != nullptr) ? child->left : child->right;

        if (parent == nullptr) {
            root = nullptr;
        } else if (parent->left == child) {
            parent->left = nextNode;
        } else {
            parent->right = nextNode;
        }
        delete child;
        return;
    }

    Node<T>* find_min(Node<T>* node) {
        if (node->left) {
            return find_min(node->left);
        }
        return node;
    }
    
    void del_node(T key) {
        auto [child, parent] = find(root, nullptr, key);
        
        // not found
        if (child == nullptr) {
            return;
        }
        
        // leave node only
        if (child->left == nullptr && child->right == nullptr) {
            delete_leaf(child, parent);
            return;
        }
        // left child only
        if (child->right == nullptr || child->right == nullptr) {
            delete_one_child(child, parent);
            return ;
        }
        Node<T>* minNode = find_min(child->right);
        T minData = minNode->data;

        del_node(minData);
        child->data = minData;
    }
    
    void pprint(Node<T>* node) {
        if (node == nullptr) {
            return;
        }
        pprint(node->left);
        std::cout << node->data << " ";
        pprint(node->right);
    }
    
    void pprint_levels(Node<T>* node) {
        std::deque<Node<T>*> q;
        q.push_back(node);
        
        while (!q.empty()) {
            int lenLevel = q.size();
            for (int i = 0; i < lenLevel; ++i) {
                Node<T>* node = q.front();
                q.pop_front();
                std::cout << node->data << " ";
                if (node->left) {
                    q.push_back(node->left);
                }
                if (node->right) {
                    q.push_back(node->right);
                }
            }
            std::cout << std::endl;
        }
        
    }
    
};

int main() {
    Node<int>* left = new Node(3);
    Node<int>* right = new Node(6);
    Node<int>* node = new Node(5);
    Tree<int> t(node);
    t.add(left);
    t.add(right);
    t.add(new Node(4));
    t.add(new Node(2));
    
    t.pprint(t.root);
    t.del_node(3);
    std::cout << '\n' << std::endl;
    t.pprint_levels(t.root);
    
    return 0;
}
