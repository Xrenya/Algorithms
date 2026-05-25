#include <iostream>
#include <vector>
#include <cassert>
#include <string>

class Solution {
public:
    bool canReach(std::string s, int minJump, int maxJump) {
        int n = static_cast<int>(s.length());
        std::vector<int> f(n), prefix(n);
        f[0] = 1;
        for (int i = 0; i < minJump; ++i) {
            prefix[i] = 1;
        }
        for (int i = minJump; i < n; ++i) {
            int left = i - maxJump;
            int right = i - minJump;
            if (s[i] == '0') {
                int total = prefix[right] - (left <= 0 ? 0 : prefix[left - 1]);
                f[i] = (total != 0);
            }
            prefix[i] = prefix[i - 1] + f[i];
        }
        return f[n - 1];
    }
};

int main() {
    Solution sol;
    std::string s = "011010";
    int minJump = 2, maxJump = 3;
    bool exepectedOutput = true;
    bool output = sol.canReach(s, minJump, maxJump);
    assert((exepectedOutput == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
