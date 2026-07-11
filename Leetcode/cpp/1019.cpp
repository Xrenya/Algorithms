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
    std::vector<int> nextLargerNodes(ListNode* head) {
        ListNode* node = head;
        int n = 0;
        while (node != nullptr) {
            node = node->next;
            ++n;
        }
        
        std::vector<int> output(n, 0);
        std::priority_queue<std::pair<int, int>> pq;
        int currentIndex = 0;
        while (head != nullptr) {
            const int& value = head->val;
            while (!pq.empty() && -pq.top().first < value) {
                int index = pq.top().second;
                output[index] = value;
                pq.pop();
            }
            pq.push({-value, currentIndex});
            ++currentIndex;
            head = head->next;
        }
        return output;
    }
};
