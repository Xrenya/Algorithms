#include <iostream>
#include <unordered_map>
#include <set>
#include <cassert>
#include <vector>

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
    ~Node() {
        if (next != nullptr) {
            delete next;    
        }
        
        if (random != nullptr) {
            delete random;    
        }
    }
};

class Solution {
private:
    std::unordered_map<Node*, Node*> umap;

public:
    Node* dfs(Node* node) {
        if (node == nullptr) {
            return node;
        }
        if (umap.contains(node)) {
            return umap[node]; 
        }
        Node* ptr = new Node(node->val);
        umap[node] = ptr;
        if (node->next != nullptr) {
            ptr->next = dfs(node->next);
        }
        if (node->random != nullptr){
            ptr->random = dfs(node->random);
        }
        return ptr;
    }

    Node* copyRandomList(Node* head) {
        umap.clear();
        return dfs(head);
    }
};

class SolutionV2 {
private:
    std::unordered_map<Node*, Node*> umap;

public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;
        if (umap.contains(head)) {
            return umap[head];
        }
        Node * node = new Node(head->val);
        umap[head] = node;
        if (head->random) {
            node->random = copyRandomList(head->random);
        }
        if (head->next) {
            node->next = copyRandomList(head->next);
        }
        return node;
    }
};

int main() {
    Solution sol;
    Node* head = new Node(1);
    Node* head2 = new Node(2);
    head->next = head2;
    head2->random = head2;
    
    Node* ptr = sol.copyRandomList(head);
    assert(((ptr->val == 1) && (ptr->next->val == 2) && (ptr->next->random->val == 2)) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
