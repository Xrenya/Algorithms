int longestSubarray(int* nums, int numsSize) {
    int zeros = 0, max_len = 0, left = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 0) {
            zeros++;
        }
        while (zeros > 1) {
            if (nums[left++] == 0) {
                zeros--;
            }
        }
        max_len = max_len > i - left ? max_len : i - left;
    }
    return max_len;
}
