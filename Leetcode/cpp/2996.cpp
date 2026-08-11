class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int n = nums.size();
        std::unordered_set<int> set(nums.begin(), nums.end());
        int total = nums[0];

        for (int i = 1; i < n; ++i) {
            if (nums[i] - 1 == nums[i - 1]) {
                total += nums[i];
            } else {
                break;
            }
        }

        while (set.contains(total)) {
            ++total;
        }

        return total;
    }
};
