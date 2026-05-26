#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <cassert>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
    ~ListNode() {
    ListNode* current = this;
    while (current) {
        ListNode* next = current->next;
        current->next = nullptr;  // Prevent recursive deletion
        delete current;
        current = next;
    }
}
};

class Solution {
private:
    ListNode* ptr = nullptr;
    int mid = 0;

public:
    bool dfs(ListNode*& node, int index) {
        if (node != nullptr) {
            if (!dfs(node->next, index + 1)) {
                if (index >= mid) {
                    std::swap(ptr->val, node->val);
                    ptr = ptr->next;
                }
            }
        }
        return false;
    }

    ListNode* reverseList(ListNode* head) {
        int count = 0;
        ListNode* node = head;
        while (node) {
            node = node->next;
            ++count;
        }
        mid = count / 2;
        ptr = head;
        dfs(head, 0);
        return head;
    }
};
bool cmpListNodes(ListNode* left, ListNode* right) {
    while (left != nullptr && right != nullptr) {
        if (left->val == right->val) {
            left = left->next;
            right = right->next;
        } else {
            return false;
        }
    }
    if ((left != nullptr && right == nullptr )|| (left == nullptr && right != nullptr)) {
        return false;
    }
    return true;
}

int main() {
    Solution sol;
    ListNode* expectedOutput = new ListNode(3, new ListNode(2, new ListNode(1)));
    ListNode* head = new ListNode(1, new ListNode(2, new ListNode(3)));
    ListNode* output = sol.reverseList(head);
    
    assert(cmpListNodes(expectedOutput, output) && "Test #1 failed!");
    
    head = new ListNode(1, new ListNode(2, new ListNode(3)));
    
    std::cout << "Tests are passed!" << std::endl;
    delete head, output, expectedOutput;
    return 0;
}
