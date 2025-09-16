/**
 * Note: The returned array must be malloced, assume caller calls free().
*/

#include <stdlib.h>


int gcd(int a, int b) {
    while (b) {
        a %= b;
        int tmp = a;
        a = b;
        b = tmp;
    }
    return a;
}

int* replaceNonCoprimes(int* nums, int numsSize, int* returnSize) {
    int *output = (int *) malloc(sizeof(int) * numsSize);
    int size = 0;
    for (int i = 0; i < numsSize; ++i) {
        int cur_num = nums[i];
        while (size > 0 && gcd(output[size - 1], cur_num) > 1) {
            int last_num = output[size - 1];
            
            size--;

            int common_divisor = gcd(last_num, cur_num);
            cur_num = (last_num / common_divisor) * cur_num;
        }
        output[size++] = cur_num;
    }
    *returnSize = size;
    return output;

}
