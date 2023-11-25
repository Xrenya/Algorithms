class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        int left_sum = 0, n = nums.size(), total =  std::accumulate(nums.begin(), nums.end(), 0);
        std::vector<int> output;
        for (int i = 0; i < nums.size(); i++) {
            int right_sum = total - left_sum - nums[i];

            int left_count = i;
            int right_count = n - 1 - i;

            int total_left = nums[i] * left_count - left_sum;
            int total_right = right_sum - nums[i] * right_count;
            output.push_back(total_left + total_right);
            left_sum += nums[i];
        }
        return output;
    }
};
