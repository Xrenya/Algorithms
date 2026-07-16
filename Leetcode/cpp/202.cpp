class Solution {
public:
    bool isHappy(int n) {
        std::set<int> seen;

        while (n > 1) {
            int tmp = 0;
            while (n) {
                tmp += (n % 10) * (n % 10);
                n /= 10;
            }
            if (seen.contains(tmp)) {
                return false;
            }
            seen.insert(tmp);
            n = tmp;
        }
        return n == 1;
    }
};
