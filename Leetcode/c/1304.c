/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumZero(int n, int* returnSize) {
    *returnSize = n;
    int *output = malloc(n * sizeof(int));
    int index = 0;
    for (int i = 1; i <= n / 2; ++i) {
        output[index++] = i;
        output[index++] = -i;        
    }
    if (n %  2 == 1) {
        output[index] = 0;
    }
    return output;
}
