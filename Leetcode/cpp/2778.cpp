class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int acc = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if ((nums.size() % (i + 1)) == 0) {
                acc += (nums[i] * nums[i]);
            }
        }
        return acc;
    }
};
