class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        vector<int> min_array(n);
        min_array[0] = nums[0];
        for (int i = 1; i < n; i++){
            min_array[i] = (min_array[i - 1] < nums[i])? min_array[i - 1] : nums[i];
        };
        stack<int> stack;
        for (int i = n - 1; i > 0; i--){
            if (nums[i] <= min_array[i]){
                continue;
            };
            
            while (!stack.empty() && stack.top() <= min_array[i]){
                stack.pop();
            };
            
            if (!stack.empty() && stack.top() < nums[i]){
                return true;
            };
            stack.push(nums[i]);
        }; 
    return false;
    }
};
