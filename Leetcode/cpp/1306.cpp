#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <queue>

class Solution {
public:
    bool canReach(std::vector<int>& arr, int start) {
        size_t n = arr.size();

        std::queue<int> q;
        q.push(start);

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            if (arr[node] == 0) {
                return true;
            }
            if (arr[node] > 0) {
                if (node + arr[node] < n) {
                    q.push(node + arr[node]);
                }
                if (node - arr[node] >= 0) {
                    q.push(node - arr[node]);
                }
                arr[node] = -arr[node];
            }
        }
        return false;
    }
    int dfs(int index, std::vector<int>& arr, std::set<int>& visited) {
        if (index < 0 || index > arr.size() - 1) {
            return -1;
        }
        if (arr[index] ==  0) {
            return 1;
        }
        int output = 0;
        visited.insert(index);
        int forward_index = index+ arr[index];
        if (!visited.contains(forward_index)) {
            output = dfs(forward_index, arr, visited);
        }
        if (output == 1) {
            return 1;
        }
        int backward_index = index - arr[index];
        if (!visited.contains(backward_index)) {
            output = dfs(backward_index, arr, visited);
        }
        visited.erase(index);
        if (output == 1) {
            return 1;
        }
        return 0;
    }
    bool canReachDfs(std::vector<int>& arr, int start) {
        std::set<int> visited;
        return dfs(start, arr, visited);
    }
};


int main() {
    Solution sol;
    std::vector<int> arr = {4, 2, 3, 0, 3, 1, 2};
    int start = 5;
    bool exected_output = true;
    int output = sol.canReach(arr, start);
    assert((exected_output == output) && "Test #1 failed!");
    
    output = sol.canReachDfs(arr, start);
    assert((exected_output == output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
