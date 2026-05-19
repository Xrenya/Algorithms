#include <iostream>
#include <vector>
#include <cassert>
#include <deque>

class Solution {
public:
    int timeRequiredToBuyV2(std::vector<int>& tickets, int k) {
        std::deque<int> q(tickets.begin(), tickets.end());
        int size = static_cast<int>(tickets.size());
        int time = 0;
        while (true) {
            int front = q.front();
            q.pop_front();
            --front;
            ++time;
            if (front == 0 && k == 0) {
                return time;
            }
            if (front > 0) {
                q.push_back(front);
            }
            if (k == 0) {
                k = static_cast<int>(q.size()) - 1;
            } else {
                --k;
            }
        }
        return -1;
    }
    
    int timeRequiredToBuy(std::vector<int>& tickets, int k) {
        int time = 0;
        int target = tickets[k];
        
        for (int i = 0; i < tickets.size(); ++i) {
            if (i <= k) {
                time += std::min(tickets[i], target);
            } else {
                time += std::min(tickets[i], target - 1);
            }
        }
        
        return time;
    }
};

int main() {
    Solution sol;
    std::vector<int> tickets = {2, 3, 2};
    int k = 2;
    int expected_output = 6;
    int output = sol.timeRequiredToBuy(tickets, k);
    
    assert((expected_output == output) && "Test #1 failed!");
    
    output = sol.timeRequiredToBuyV2(tickets, k);
    assert((expected_output == output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
