#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>


class Solution {
private:
    std::vector<int> root;
    std::vector<int> rank;

    int find(int x) {
        if (root[x] != x) {
            root[x] = find(root[x]);
        }
        return root[x];
    }

    void Union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) {
            return;
        }
        if (rank[x] < rank[y]) {
            std::swap(x, y);
        }
        root[y] = x;
        if (rank[x] == rank[y]) {
            rank[x]++;
        }
    }


public:
    int minimumHammingDistance(std::vector<int>& source, std::vector<int>& target, std::vector<std::vector<int>>& allowedSwaps) {
        int n = source.size();
        root.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; ++i) {
            root[i] = i;
        }
        for (auto pair : allowedSwaps) {
            Union(pair[0], pair[1]);
        }
        std::unordered_map<int, std::unordered_map<int, int>> sets;
        for (int i = 0; i < n; ++i) {
            int x = find(i);
            sets[x][source[i]]++;
        }
        int output = 0;
        for (int i = 0; i < n; ++i) {
            int x = find(i);
            if (sets[x][target[i]] > 0) {
                sets[x][target[i]] -= 1;
            } else {
                ++output;
            }
        }
        return output;

    }
};

int main()
{
    
    
    std::vector<int> source = {1,2,3,4}, target = {2,1,4,5};
    std::vector<std::vector<int>> allowedSwaps = {{0,1},{2,3}};
    int expected_output = 1;
    
    Solution sol;
    int output = sol.minimumHammingDistance(source, target, allowedSwaps);
    assert ((expected_output == output) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;

    return 0;
}
