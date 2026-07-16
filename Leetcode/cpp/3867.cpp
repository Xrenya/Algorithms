class Solution {
public:
    long long gcd(long long a, long long b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
    long long gcdSum(vector<int>& nums) {
        long long el = nums[0];
        std::vector<long long > prefixGcd;
        for (int i = 0; i < nums.size(); ++i) {
            if (el < nums[i]) {
                el = nums[i];
            }
            prefixGcd.push_back(gcd(el, nums[i]));
        }
        std::sort(prefixGcd.begin(), prefixGcd.end());

        long long output = 0;
        int left = 0;
        int right = prefixGcd.size() - 1;
        while (left < right) {
            output += gcd(prefixGcd[right], prefixGcd[left]);
            ++left;
            --right;
        }
        return output;
    }
};
