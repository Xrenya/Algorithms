class Solution {
public:
    int countHillValley(vector<int>& nums) {
        vector<int> output;
        for (int i = 0; i < nums.size(); i++) {
            if (output.size() == 0) {
                output.push_back(nums[i]);
            } else if (output[output.size() - 1] != nums[i]) {
                output.push_back(nums[i]);
            }
        }
        int counter = 0; 
        for (int i = 1; i < output.size() - 1; i++) {
            if ((output[i - 1] < output[i] && output[i + 1] < output[i]) || (output[i - 1] > output[i] && output[i + 1] > output[i])) {
                counter++;
            }
        }
        return counter;
    }
};
