class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        vector<int> output;
        unordered_map<int, int> count;
        for (int i = 0; i < nums.size(); ++i) {
            if (count[nums[i]] > 0) {
                output.push_back(nums[i]);
            }
            count[nums[i]]++;
        }
        return output;
    }
};
