class Solution {
public:
    void pprint(std::vector<int>& ar) {
        for (const auto& val : ar) {
            std::cout << val << " "; 
        }
        std::cout << std::endl;
    } 
    int waysToMakeFair(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> prefix_even(n + 1, 0);
        std::vector<int> prefix_odd(n + 1, 0);
        std::vector<int> suffix_even(n + 1, 0);
        std::vector<int> suffix_odd(n + 1, 0);
        for (int i = 1; i < n + 1; ++i) {
            if ((i - 1) % 2 == 0) {
                prefix_even[i] = prefix_even[i - 1] + nums[i - 1];
                prefix_odd[i] = prefix_odd[i - 1];
            } else {
                prefix_even[i] = prefix_even[i - 1];
                prefix_odd[i] = prefix_odd[i - 1] + nums[i - 1];
            }
        }
        for (int i = n - 1; i >= 0; --i) {
            if (i % 2 == 0) {
                suffix_even[i] = suffix_even[i + 1] + nums[i];
                suffix_odd[i] = suffix_odd[i + 1];
            } else {
                suffix_even[i] = suffix_even[i + 1];
                suffix_odd[i] = suffix_odd[i + 1] + nums[i];
            }
        }
        // pprint(prefix_even);
        // pprint(prefix_odd);
        // pprint(suffix_even);
        // pprint(suffix_odd);
        int count = 0;
        for (int i = 0; i < n; ++i) {
            if (prefix_even[i] + suffix_odd[i + 1] == prefix_odd[i] + suffix_even[i + 1]) {
                ++count;
            }
        }
        return count;
    }
};
