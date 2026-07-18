class Solution {
public:
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    int findGCD(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        return gcd(nums.back(), nums[0]);
    }
};
