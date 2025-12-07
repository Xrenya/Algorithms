#include <stdio.h>
#include <time.h>

/* binary search */
int binarysearch(int x, int v[], int n) {
    int low = 0;
    int high = n - 1;
    int mid;
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else
            return mid;
    }
    return -1;

}

int binary_search_one(int x, int v[], int n) {
    int low = 0;
    int high = n - 1;
    int mid;
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (x < v[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    return (low > 0 && v[low - 1] == x) ? low - 1 : -1;
}

int main() {
    clock_t start_time, end_time;
    double cpu_time_used;
    int v[] = {1, 2, 3, 4, 5, 6};
    int x = 6;
    start_time = clock();
    printf("%d\n", binarysearch(x, v, sizeof(v) / sizeof(int)));
    end_time = clock();
    cpu_time_used = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
    printf("CPU time used: %f seconds\n", cpu_time_used);
    
    start_time = clock();
    printf("%d\n", binary_search_one(x, v, sizeof(v) / sizeof(int)));
    end_time = clock();
    cpu_time_used = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
    printf("CPU time used: %f seconds\n", cpu_time_used);
    return 0;
}
