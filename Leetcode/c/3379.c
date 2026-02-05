/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

int* constructTransformedArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int *result = (int*)malloc(numsSize * sizeof(nums));
    for (int i = 0; i < numsSize; ++i) {
        result[i] = nums[((i + nums[i]) % numsSize + numsSize) % numsSize]; 
    }
    return result;
}
