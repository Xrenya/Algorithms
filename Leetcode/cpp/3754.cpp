class Solution {
public:
    long long sumAndMultiply(int n) {
        long long size = 1;
        int digit = n;
        while (digit) {
            size *= 10;
            digit /= 10;
        }
        digit = n;
        size /= 10;
        long long output = 0;
        long long mult;
        while (size > 0) {
            int lastDigit = (digit / size) % 10;
            size /= 10;
            if (lastDigit) {
                output = output * 10 + lastDigit;
                mult += lastDigit;
            }   
        }
        return output * mult;
    }
    long long sumAndMultiplyV2(int n) {
        long long tmp = 0;
        int copy = n;
        int power = 0;
        long long acc = 0;
        while (copy) {
            long long lastDigit = copy % 10;
            if (lastDigit) {
                acc += lastDigit;
                lastDigit *= pow(10, power++);
            }
            tmp += lastDigit;
            copy /= 10;
        }
        return tmp * acc;
    }
};
