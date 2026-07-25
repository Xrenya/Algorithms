class Solution {
public:
    int maxProduct(int n) {
        int first = 0;
        int second = 0;
        while (n) {
            int digit = n % 10;
            if (first <= digit) {
                second = first;
                first = digit;
            } else if (second <= digit) {
                second = digit;
            }
            n /= 10;
        }
        return first * second;
    }
};
