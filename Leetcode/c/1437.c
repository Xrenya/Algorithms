bool kLengthApart(int* nums, int numsSize, int k) { 
    int prev = -1;
    int dist = INT_MAX;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            if (dist < k) {
                return false;
            }
            dist = 0;
            prev = i;
        } else {
            if (dist != INT_MAX) {
                dist++;
            };
        }
    }
    return true;
}
