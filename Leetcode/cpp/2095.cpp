/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
#include <cassert>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        fast = fast->next->next;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }

        slow->next = slow->next->next;
        return head;
    }
    ListNode* deleteMiddleV2(ListNode* head) {
        if (head == nullptr) {
            return head;
        }
        int count = 0;
        ListNode* node = head;
        while (node) {
            node = node->next;
            ++count;
        }
        if (count == 1) {
            return nullptr;
        }
        node = head;
        if (count % 2 == 0) {
            count = count / 2 - 1;
        } else {
            count = count / 2 - 1;
        }
        for (int i = 0; i < count; ++i) {
            node = node->next; 
        }
        if (node->next != nullptr) {
            node->next = node->next->next != nullptr ? node->next->next : nullptr;
        }
        return head;
    }
};

int main()
{
    Solution sol;
    std::vector<int> nodes = {3, 4, 7, 1, 2, 6};
    ListNode* node = new ListNode(1);
    ListNode* head = node;;
    for (auto val : nodes) {
        node->next = new ListNode(val);
        node = node->next;
    }
    ListNode* output = sol.deleteMiddle(head);
    while (output) {
        assert((output->val != 7) && "Test #1 failed!");
        output = output->next;
    }
    std::cout << "Tests are passed!" << std::endl;;

    return 0;
}
