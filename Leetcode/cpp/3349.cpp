class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int count = 1, prec = 0, output = 0;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1]) {
                count += 1;
            } else {
                prec = count;
                count = 1;
            }
            output = std::max(output, std::min(prec, count));
            output = std::max(output, count / 2);
        }
        return output >= k;
    }
};
