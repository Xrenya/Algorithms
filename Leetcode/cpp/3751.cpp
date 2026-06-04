#include <iostream>
#include <cassert>
#include <string>

class Solution {
public:
    int totalWaviness(int num1, int num2) {
        auto getWaviness = [](int x) {
            std::string s = std::to_string(x);
            int waviness = 0;

            for (size_t i = 1; i < s.size() - 1; ++i) {
                bool isPeak = s[i] > s[i - 1] && s[i] > s[i + 1];
                bool isValley = s[i] < s[i - 1] && s[i] < s[i + 1];
                if (isPeak || isValley) {
                    ++waviness;
                }
            }
            return waviness;
        };

        int total = 0;
        for (int i = num1; i <= num2; ++i) {
            total += getWaviness(i);
        }
        return total;
    }
};


int main() {
    Solution sol;
    int num1 = 120, num2 = 130;
    int expectedOutput = 3;
    int output = sol.totalWaviness(num1, num2);
    
    assert((output == expectedOutput) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
