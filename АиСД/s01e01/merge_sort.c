#include <stdio.h>

void merge(int array[], int ptr_left, int ptr_middle, int ptr_right) {
     int size_left = ptr_middle - ptr_left + 1;
     int size_right = ptr_right - ptr_middle;
     
     int left[size_left];
     int right[size_right];
     
     for (int i = 0; i < size_left; ++i) {
         left[i] = array[ptr_left + i];
     }
     for (int j = 0; j < size_right; ++j) {
         right[j] = array[ptr_middle + j + 1];
     }
     
     int i = 0;
     int j = 0;
     int k = ptr_left;
     
     while (i < size_left && j < size_right) {
         if (left[i] <= right[j]) {
             array[k++] = left[i++];
         } else {
             array[k++] = right[j++];
         }
     }
     while (i < size_left) {
         array[k++] = left[i++];
     }
     while (j < size_right) {
         array[k++] = right[j++];
     }
}

void sort(int array[], int left, int right) {
    if (left < right) {
        int ptr_middle = left + (right - left) / 2;
        sort(array, left, ptr_middle);
        sort(array, ptr_middle + 1, right);
        merge(array, left, ptr_middle, right);
    }
}


int main() {
    int array[6] = {5,4,3,0,2,1};
    
    int ptr_right = sizeof(array) / sizeof(array[0]) - 1;
    int ptr_left = 0;
    
    sort(array, ptr_left, ptr_right);
    for (int i = 0; i < ptr_right + 1; ++i) {
        printf("%d ", array[i]);
    }
    return 0;
}
