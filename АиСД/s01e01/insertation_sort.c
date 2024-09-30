#include <stdio.h>

int main() {
    int a[5] = {5, 4, 3, 2, 1};
    int size = sizeof(a) / sizeof(a[0]);
    for (int i = 0; i < size; ++i) {
        int j = i;
        while (j > 0 && a[j] < a[j - 1]) {
            int temp = a[j - 1];
            a[j - 1] = a[j];
            a[j] = temp;
            j--;
        }
    }
    for (int i = 0; i < size; ++i) {
        printf("%d ", a[i]); // output: '1 2 3 4 5 '
    }
    return 0;
}
