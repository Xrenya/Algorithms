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
    ListNode* oddEvenListWithCounting(ListNode* head) {
        ListNode* tail = head;
        int totalNumsNodes = 0;
        while (tail != nullptr && tail->next != nullptr) {
            tail = tail->next;
            ++totalNumsNodes;
        }
        if (totalNumsNodes <= 1) { // defualt return
            return head;
        }
        ListNode* cur = head;
        for (int i = 0; i < totalNumsNodes; i += 2) {
            ListNode* nextNode = cur->next;
            if (nextNode->next != nullptr) {
                cur->next = nextNode->next;
            } else {
                cur->next = nullptr;
            }
            nextNode->next = nullptr;
            tail->next = nextNode;
            tail = tail->next;
            cur = cur->next;
        }
        return head;
    }
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* odd = head;
        ListNode* evenHead = head->next;
        ListNode* even = evenHead;
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        odd->next = evenHead;
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
    ListNode* expectedOutput = new ListNode(1, new ListNode(3, new ListNode(2)));
    ListNode* head = new ListNode(1, new ListNode(2, new ListNode(3)));
    ListNode* output = sol.oddEvenListWithCounting(head);
    
    assert(cmpListNodes(expectedOutput, output) && "Test #1 failed!");
    
    head = new ListNode(1, new ListNode(2, new ListNode(3)));
    output = sol.oddEvenList(head);
    
    assert(cmpListNodes(expectedOutput, output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    delete head, output, expectedOutput;
    return 0;
}
