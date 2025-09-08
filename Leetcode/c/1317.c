/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getNoZeroIntegers(int n, int* returnSize) {
    char a_str[8], b_str[8];
    for (int a = 1; a < n; ++a) {
        int b = n - a;
        sprintf(a_str, "%d", a);
        sprintf(b_str, "%d", b);
        if (strchr(a_str, '0') == NULL && strchr(b_str, '0') == NULL) {
            int *output = malloc(2 * sizeof(int));
            *returnSize = 2;
            output[0] = a;
            output[1] = b;
            return output;
        }
    }
    *returnSize = 0;
    return NULL;
}
