#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    int fixedPoint(std::vector<int>& arr) {
        for (int i = 0; i < arr.size(); ++i) {
            if (i == arr[i]) return i;
        }
        return -1;
    }
};

int main() {
    Solution sol;
    std::vector<int> arr = {-10, -5, 0, 3, 7};
    int expected_output = 3;
    
    int output = sol.fixedPoint(arr);
    assert((expected_output == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
