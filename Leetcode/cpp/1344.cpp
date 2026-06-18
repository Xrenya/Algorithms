#include <iostream>
#include <cassert>

class Solution {
public:
    double angleClock(int hour, int minutes) {
        double hour_ = (hour % 12 )* 30.0 + minutes * 0.5;;
        double minutes_ = minutes * 6.0;
        double x = std::abs(hour_ - minutes_);
        return std::min<double>(x, 360.0 - x);
    }
};

int main() {
    Solution sol;
    int hour = 12, minutes = 30;
    double expectedOutput = 165;
    double output = sol.angleClock(hour, minutes);
    
    assert((output == expectedOutput) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
