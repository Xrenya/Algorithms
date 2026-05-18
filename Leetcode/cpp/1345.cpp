#include <iostream>
#include <queue>
#include <map>
#include <cassert>
#include <set>


class Solution {
public:
    int minJumps(std::vector<int>& arr) {
        int n = static_cast<int>(arr.size());
        if (n <= 1) {
            return 0;
        }

        std::map<int, std::vector<int>> graph;
        for (int i = 0; i < n; ++i) {
            graph[arr[i]].push_back(i);
        }
        std::set<int> visited;
        std::queue<int> q;
        visited.insert(0);
        q.push(0);
        int steps = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                int node = q.front();
                q.pop();

                if (node == n - 1) {
                    return steps;
                }

                for (auto next_index : graph[arr[node]]) {
                    if (!visited.contains(next_index)) {
                        visited.insert(next_index);
                        q.push(next_index);
                    }
                }
                graph[arr[node]] = {};

                for (auto nei : {node - 1, node + 1}) {
                    if (nei >= 0 && nei < n && !visited.contains(nei)) {
                        visited.insert(nei);
                        q.push(nei);
                    }
                }
            }
        ++steps;
        }
        return -1;
    }
};
int main() {
    Solution sol;
    std::vector<int> arr = {100, -23, -23, 404, 100, 23, 23, 23, 3, 404};
    int expected_output = 3;
    int output = sol.minJumps(arr);
    
    assert((expected_output == output) && "Test #1 failed!");
    
    arr = {100};
    expected_output = 0;
    output = sol.minJumps(arr);
    
    assert((expected_output == output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
