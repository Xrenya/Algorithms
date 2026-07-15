class Solution {
public:
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    int gcdOfOddEvenSums(int n) {
        int odd = 0;
        int even = 0;
        for (int i = 1; i <= n; ++i) {
            odd += 2 * i - 1;
            even += 2 * i;
        }
        return gcd(odd, even);
    }
};
