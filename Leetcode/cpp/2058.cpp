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
public:
    std::vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        std::vector<int> output = {-1, -1};
        if (!head->next || !head->next->next) {
            return output;
        }
        std::vector<int> array;
        int prev_dist = 100001;
        int prev_index = -1;
        ListNode* prev_node = head;
        ListNode* node = head->next;
        ListNode* next_node = head->next->next;
        int index = 1;
        while (next_node) {
            if (node->val > prev_node->val && node->val > next_node->val) {
                array.push_back(index);
                if (prev_index != -1) {
                    prev_dist = min(prev_dist, index - prev_index);
                }
                prev_index = index;
            }

            if (node->val < prev_node->val && node->val < next_node->val) {
                array.push_back(index);
                if (prev_index != -1) {
                    prev_dist = min(prev_dist, index - prev_index);
                }
                prev_index = index;
            }
            ++index;
            next_node = next_node->next;
            prev_node = prev_node->next;
            node = node->next;
        }
        if (array.size() < 2) {
            return output;
        }
        output = {prev_dist, array.back() - array.front()};
        return output;
    }
};
