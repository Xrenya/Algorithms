#include <stdio.h>


void swap(int v[], int i, int j) {
    int temp;
    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}


void qsort(int v[], int left, int right) {
    int i, last;
    // void swap(int v[], int i, int j);
    if (left >= right) {
        return;
    }
    swap(v, left, (left + right) / 2);
    last = left;
    for (i = left + 1; i <= right; ++i) {
        if (v[i] < v[left]) {
            swap(v, ++last, i);
        }
    }
    swap(v, left, last);
    qsort(v, left, last - 1);
    qsort(v, last + 1, right);
}

int main() {
    // Write C code here
    int n[] = {5, 0, 4, 10, -10, 3, 2, 1, -1, -2};
    int left = 0, right = sizeof(n) / sizeof(int) - 1;
    qsort(n, left, right);
    for (int i = 0; i <= right; ++i) {
        printf("%d ", n[i]);
    }
    return 0;
}
