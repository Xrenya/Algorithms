class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> suffix(n + 1, 1), prefix(n + 1, 1), output;

        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] * nums[i];
            suffix[n - i - 1] = suffix[n - i] * nums[n - 1 - i];
        }

        // for (int i = 0; i < n + 1; ++i) {
        //     std::cout << prefix[i] << " ";
        // }
        // std::cout << std::endl;
        // for (int i = 0; i < n + 1; ++i) {
        //     std::cout << suffix[i] << " ";
        // }

        for (int i = 0; i < n; ++i) {
            output.push_back(prefix[i] * suffix[i + 1]);
        }
        return output;
    }
};
