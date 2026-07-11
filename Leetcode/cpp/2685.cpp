class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        std::vector<std::vector<int>> graph(n, std::vector<int>());

        std::unordered_map<std::string, int> umap;

        for (int i = 0; i < n; ++i) {
            graph[i].push_back(i);
        }

        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        for (int i = 0; i < n; ++i) {
            std::vector<int> nodes = graph[i];
            std::sort(nodes.begin(), nodes.end());
            std::string key;

            for (const auto& node : nodes) {
                key += std::to_string(node) + ",";
            }
            ++umap[key];
        }
        int counter = 0;
        for (const auto& entry : umap) {
            int size = std::count(entry.first.begin(), entry.first.end(), ',');
            if (size == entry.second) {
                ++counter;
            }
        }
        return counter;
    }
};
