#include <iostream>
#include <tuple>
#include <vector>
#include <climits>
#include <queue>

class Solution {
public:
    int minCost(int n, vector<vector<int>>& edges) {
        std::vector<std::vector<std::tuple<int, int>>> q(n);
        for (auto edge : edges) {
            q[edge[0]].push_back(std::make_tuple(edge[1], edge[2]));
            q[edge[1]].push_back(std::make_tuple(edge[0], 2 * edge[2]));
        }

        std::vector<int> distance(n, INT_MAX);
        std::vector<bool> visited(n, false);
        std::priority_queue<std::tuple<int, int>,
                            std::vector<std::tuple<int, int>>,
                            std::greater<std::tuple<int, int>>> pq;
        distance[0] = 0;
        pq.push(std::make_tuple(0, 0));

        while (!pq.empty()) {
            auto [dist, node] = pq.top();
            pq.pop();

            if (visited[node]) {
                continue;
            }

            visited[node] = false;

            if (node == n - 1) {
                return distance[node];
            }

            for (auto [next_node, dist] : q[node]) {
                if (distance[node] + dist < distance[next_node]) {
                    distance[next_node] = distance[node] + dist;
                    pq.push(std::make_tuple(distance[next_node], next_node));
                }
            }
        }
        return -1;
    }
};
