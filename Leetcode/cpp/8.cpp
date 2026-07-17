class Solution {
public:
    int myAtoi(string s) {
        long long output = 0;
        int negative = 0;
        int digitsBefore = false;
        int positive = 0;
        long long maxLimit = pow(2, 31);
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == ' ') {
                if (digitsBefore || positive || negative) {
                    break;
                }
                continue;
            } else if (s[i] == '-') {
                if (digitsBefore || positive || negative) {
                    break;
                }
                negative = 1;
            }  else if (s[i] == '+') {
                if (digitsBefore || negative || positive) {
                    break;
                }
                positive = 1;
            } else if (std::isdigit(s[i])) {
                int num = s[i] - '0';
                if (output >= maxLimit) {
                    output = maxLimit;
                } else {
                    output = output * 10 + num;
                }
                digitsBefore = true;
            } else {
                break;
            }
        }
        if (negative) {
            output *= -1;
        }
        output = std::min<long long>(output, (long long) pow(2, 31) - 1);
        output = std::max<long long>(output, (long long) pow(2, 31) * -1);
        return output;
    }
};
