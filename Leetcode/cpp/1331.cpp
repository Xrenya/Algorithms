class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        std::priority_queue<std::pair<int, int>> pq;
        for (int i = 0; i < arr.size(); ++i) {
            pq.push({-arr[i], i});
        }
        std::vector<int> output(arr.size(), 0);

        int idx = 0;
        int prev = INT_MAX;
        while (!pq.empty()) {
            auto [value, index] = pq.top();
            pq.pop();
            if (prev != -arr[index]) {
                ++idx;
            }       
            output[index] = idx;
            prev = -arr[index];
        }

        return output;
    }
    vector<int> arrayRankTransformSet(vector<int>& arr) {
        std::set<int> set;
        std::unordered_map<int, int> umap;

        for (auto val : arr) {
            set.emplace(val);
        }
        int index = 1;
        for (auto val : set) {
            umap[val] = index++;
        }

        std::vector<int> output;

        for (auto val : arr) {
            output.push_back(umap[val]);
        }
        return output;
    }
};
