class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++){
            if (1 == map.count(nums[i]) and abs(i - map[nums[i]]) <= k){
                return true;
            }
            map[nums[i]] = i;
        }
        return false;
    }
};

class SolutionV2 {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::unordered_map<int, std::vector<int>> umap;
        for (int i = 0; i < nums.size(); ++i) {
            umap[nums[i]].push_back(i);
        }

        for (const auto& [num, ar] : umap) {
            if (ar.size() < 2) {
                continue;
            }
            for (int j = 1; j < ar.size(); ++j) {
                if (ar[j] - ar[j - 1] <= k) {
                    return true;
                }
            }
        }
        return false;
    }
};
