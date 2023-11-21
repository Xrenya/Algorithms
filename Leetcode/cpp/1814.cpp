class Solution {
public:
    int rev(int n) {
        int acc = 0;
        while (n > 0) {
            acc = acc * 10 + n % 10;
            n /= 10;
        }
        return acc;
    } 
    int countNicePairs(vector<int>& nums) {
        vector<int> arr;
        unordered_map<int, int> dict;
        int output = 0, MOD = 1e9 + 7;
        for (int i = 0; i < nums.size(); i++) {
            arr.push_back(nums[i] - rev(nums[i]));
        }
        for (int num : arr) {
            output = (output + dict[num]) % MOD;
            dict[num]++;
        }
        return output;
    }
};
