class Solution {
public:
    int romanToInt(string s) {
        std::unordered_map<char, std::pair<int, int>> umap = {
            {'I', {0, 1}}, {'V', {1, 5}}, {'X', {2, 10}}, {'L', {3, 50}}, {'C', {4, 100}}, {'D', {5, 500}}, {'M', {6, 1000}}
        };
        int output = 0;
        for (int i = s.length() - 1; i >= 0; --i) {
            if (i < s.length() - 1 && umap[s[i]].first < umap[s[i + 1]].first) {
                output -= umap[s[i]].second;
            } else {
                output += umap[s[i]].second;
            }
        }
        return output;
    }
};
