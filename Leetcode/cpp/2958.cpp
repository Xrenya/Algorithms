class Solution {
public:
    int maxSubarrayLength(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> map;
        int left = 0;
        int max_len = 0;
        for (int right = 0; right < nums.size(); ++right) {
            int num = nums[right];
            ++map[num];
            while (map[num] > k) {
                int remove = nums[left++];
                --map[remove];
            }
            max_len = std::max<int>(max_len, right - left + 1);
        }
        return max_len;
    }
};
