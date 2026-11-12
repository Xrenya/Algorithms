int maxValue(int a, int b) {
    if (a > b) return a;
    return b;
}

int longestMonotonicSubarray(int* nums, int numsSize) {
        int dec = 1;
        int inc = 1;
        int cur = 1;
        for (int i = 0; i < numsSize - 1; ++i) {
            if (nums[i] > nums[i + 1]) {
                ++dec;
                inc = 1;
            } else if (nums[i] < nums[i + 1]) {
                ++inc;
                dec = 1;
            } else {
                dec = 1;
                inc = 1;
            }
            cur = maxValue(cur, maxValue(dec, inc));
        }
        return cur;
}
