#include <iostream>


class Solution {
public:
    int countOperations(int num1, int num2) {
        int ops = 0;
        while (num1 > 0 && num2 > 0) {
            int mul = 1;
            if (num1 > num2) {
                mul = num1 / num2 > 0 ? num1 / num2 : 1;
                num1 -= num2 * mul;
            } else {
                mul = num2 / num1 > 0 ? num2 / num1 : 1;
                num2 -= num1 * mul;
            }
            ops += mul;
        }
        return ops;
    }
};
