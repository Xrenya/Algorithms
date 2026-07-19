class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        std::unordered_map<std::string, std::unordered_map<std::string, double>> nested_map;
        for (int i = 0; i < values.size(); ++i) {
            nested_map[equations[i][0]][equations[i][1]] = values[i];
            nested_map[equations[i][1]][equations[i][0]] = 1.0 / values[i];
        }
        std::unordered_set<std::string> visited;
        
        std::function<double(std::string, std::string, double)> dfs = [&](std::string a, std::string b, double acc) -> double {
            if (nested_map.contains(a) && nested_map[a].contains(b)) {
                return acc * nested_map[a][b];
            }
            visited.insert(a);
            double res = -1.0;
            for (const auto& [key, value] : nested_map[a]) {
                if (visited.find(key) == visited.end()) {
                    double cur = dfs(key, b, acc * value);
                    if (cur != -1.0) {
                        return cur;
                    }
                }
            }
            return res;
        };
        std::vector<double> output;
        for (int i = 0; i < queries.size(); ++i) {
            std::string a = queries[i][0];
            std::string b = queries[i][1];
            if (!nested_map.contains(a) || !nested_map.contains(b)) {
                output.push_back(-1);
            } else if (a == b) {
                output.push_back(1);
            } else {
                visited.clear();
                output.push_back(dfs(a, b, 1.0));
            }
        }
        return output;
    }
};
