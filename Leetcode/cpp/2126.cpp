#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

class Solution {
public:
    bool asteroidsDestroyed(int mass, std::vector<int>& asteroids) {
        std::sort(asteroids.begin(), asteroids.end());
        long long value = static_cast<long long>(mass); 
        for (const auto& asteroid : asteroids) {
            if (value >= asteroid) {
                value += asteroid;
            } else {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution sol;
    int mass = 10;
    std::vector<int> asteroids = {3, 9, 19, 5, 21};
    bool expectedOutput = true;
    bool output = sol.asteroidsDestroyed(mass, asteroids);
    
    assert((expectedOutput == output) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
