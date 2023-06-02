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
