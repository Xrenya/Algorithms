#include <stdio.h>

void pprint(int[], int);

void shellsort(int v[], int n) {
    int gap, i, j, temp;
    
    for (gap = n / 2; gap > 0; gap /= 2) {
        for (i = gap; i < n; ++i) {
            for (j = i - gap; j >= 0 && v[j] > v[j + gap]; j-=gap) {
                temp = v[j];
                v[j] = v[j + gap];
                v[j + gap] = temp;
            }
        }
    }
}

void pprint(int v[], int n) {
    for (int i = 0; i < n; ++i) {
        printf("%d ", v[i]);
    }
    printf("\n");
}

int main() {
    int v[] = {10, 9, 8, 3, 4, 6, 1, 2};
    pprint(v, sizeof(v) / sizeof(int));
    shellsort(v, sizeof(v) / sizeof(int));
    pprint(v, sizeof(v) / sizeof(int));
    return 0;
}
