class Solution {
public:
  int minOperations(vector<int>& nums) {
    vector<int>queue;
    int ops = 0;
    for (int i = 0; i< nums.size(); ++i) {
      while (!queue.empty() && queue.back() > nums[i]) {
        queue.pop_back();
      }
      if (nums[i] == 0) continue;
      if (queue.empty() || queue.back() < nums[i]) {
        ops++;
        queue.push_back(nums[i]);
      }
    }
    return ops;
  }
};
