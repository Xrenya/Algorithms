class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        int counter = 0;
        int index = 0;
        while (counter < n) {
            int value = nums[index];
            int start = index;
            while (true) {
                int end = (start + k) % n;
                int nextValue = nums[end];
                nums[end] = value;
                value = nextValue;
                start = end;
                ++counter;
                if (end == index) {
                    break;
                }
            }
            ++index;
        }
    }
};
