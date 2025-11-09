#include <stdio.h>


int countOperations(int num1, int num2) {
    int ops = 0;
    while (num1 && num2) {
        ops += num1 / num2;
        num1 %= num2;
        int tmp = num1;
        num1 = num2;
        num2 = tmp;
    }
    return ops;
}
