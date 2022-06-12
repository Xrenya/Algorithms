class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int n = nums.size(), output = 0, left = 0, curr = 0;
        unordered_set<int> seen;
        for (int right = 0; right < n; right++){
            if (seen.find(nums[right]) != seen.end()){
                while (nums[right] != nums[left]){
                    curr -= nums[left];
                    seen.erase(nums[left]);
                    left += 1;
                }
                left += 1;
            }
            else{
                seen.insert(nums[right]);
                curr += nums[right];
            }
            output = max(output, curr);
        }
    return output;
    }
};
