class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long int total = 0;
        long int zeros = 0;
        for (auto n: nums) {
            if (n == 0) {
                zeros++;
            } else {
                zeros = 0;
            }
            total += zeros;
        }
        return total;
    }
};
