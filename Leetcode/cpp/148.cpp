#include <iostream>
#include <vector>
#include <cassert>


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* merge(ListNode* left, ListNode* right) {
        if (!left) {
            return right;
        } else if (!right) {
            return left;
        }

        ListNode dummy;
        ListNode* node = &dummy;
        while (left && right) {
            if (left->val < right->val) {
                node->next = left;
                left = left->next;
            } else {
                node->next = right;
                right = right->next;
            }
            node = node->next;
        }
        left = left ? left : right;
        while (left) {
            node->next = left;
            left = left->next;
            node = node->next;
        }
        return dummy.next;
    }

    ListNode* sort(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* left = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* right = slow->next;
        slow->next = nullptr;
        left = sort(left);
        right = sort(right);
        return merge(left, right);
    }

    ListNode* sortList(ListNode* head) {
        return sort(head);
    }
};

// int main()
// {
//     std::vector<int> data = {4,2,1,3};
//     ListNode* head = new ListNode(0);
//     ListNode* node = head;
//     for (int i = 0; i < data.size(); ++i) {
//         node->next = new ListNode(data[i]);
//         node = node->next;
//     }

//     std::vector<int> expected_output = {1, 2, 3, 4};

//     Solution sol;
//     ListNode* output = sol.sortList(head->next);

//     for (int i = 0; i < expected_output.size(); ++i) {
//         assert(output != nullptr && "Output is shorter than expected!");
//         assert(expected_output[i] == output->val && "Test #1 failed!");
//         output = output->next;
//     }
//     assert(output == nullptr && "Output has extra nodes!");

//     std::cout << "Tests are passed!" << std::endl;
//     return 0;
// }

ListNode* build(const std::vector<int>& v) {
    ListNode dummy;
    ListNode* tail = &dummy;
    for (int x : v) {
        tail->next = new ListNode(x);
        tail = tail->next;
    }
    return dummy.next;
}

std::vector<int> toVec(ListNode* head) {
    std::vector<int> v;
    while (head) { v.push_back(head->val); head = head->next; }
    return v;
}

void freeList(ListNode* head) {
    while(head){ auto n = head->next; delete head; head = n; }
}

void test(std::vector<int> in, std::vector<int> expected) {
    Solution sol;
    ListNode* head = build(in);
    ListNode* out = sol.sortList(head);
    auto result = toVec(out);
    
    assert(result == expected && "FAILED");
    freeList(out);
}

int main() {
    test({4,2,1,3}, {1,2,3,4});
    test({}, {});
    test({1}, {1});
    test({5,4,3,2,1}, {1,2,3,4,5});
    test({1,2,3,4}, {1,2,3,4});
    test({2,2,1,3,3}, {1,2,2,3,3});
    test({-1,5,3,4,0}, {-1,0,3,4,5});

    std::cout << "All tests passed!\n";
}
