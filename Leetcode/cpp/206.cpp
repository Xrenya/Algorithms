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

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
private:
    ListNode * ptr = nullptr;
    int mid = 0;
public:
    bool dfs(ListNode * node, int index) {
        if (node != nullptr) {
            if (!dfs(node->next, index + 1)) {
                if (mid <= index) {
                    std::swap(ptr->val, node->val);
                    ptr = ptr->next;
                }
            }
        }
        return false;
    }
    ListNode* reverseListRecursive(ListNode* head) {
        ptr = head;
        int total = 0;
        ListNode * cur = head;
        while (cur != nullptr) {
            cur = cur->next;
            ++total;
        }
        mid = total / 2;
        dfs(head, 0);
        return head;
    }
    ListNode* reverseList(ListNode* head) {

        ListNode * prev = nullptr;
        ListNode * cur = head;
        while (cur != nullptr) {
            ListNode * nextNode = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nextNode;
        }

        return prev;
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
