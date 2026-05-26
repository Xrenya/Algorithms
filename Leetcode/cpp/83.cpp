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
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* curr = head;
        
        // Traverse while there is a current node and a next node
        while (curr && curr->next) {
            if (curr->val == curr->next->val) {
                // Skip the next node (remove duplicate)
                curr->next = curr->next->next;
            } else {
                // Move forward only if no duplicate found
                curr = curr->next;
            }
        }
        
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
    ListNode* expectedOutput = new ListNode(1, new ListNode(2));
    ListNode* head = new ListNode(1, new ListNode(1, new ListNode(2)));
    ListNode* output = sol.deleteDuplicates(head);
    
    assert(cmpListNodes(expectedOutput, output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    delete head, output, expectedOutput;
    return 0;
}
