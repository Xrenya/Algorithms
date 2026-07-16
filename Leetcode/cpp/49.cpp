class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> output;
        
        std::unordered_map<std::string, std::vector<std::string>> umap;

        for (int i = 0; i < strs.size(); ++i) {
            std::string sortedWord = strs[i];
            std::sort(sortedWord.begin(), sortedWord.end());
            umap[sortedWord].push_back(strs[i]);
        }

        for (const auto& [k, v] : umap) {
            output.push_back(v);
        }

        return output;
    }
};
