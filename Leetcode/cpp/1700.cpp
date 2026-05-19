#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    int countStudents(std::vector<int>& students, std::vector<int>& sandwiches) {
        int n = static_cast<int>(students.size());
        int count[2] = {0, 0};
        for (auto s : students) {
            ++count[s];
        }

        for (auto s : sandwiches) {
            if (count[s] == 0) {
                break;
            }
            --count[s];
        }

        return count[0] + count[1];
    }
};

int main() {
    Solution sol;
    std::vector<int> students = {1, 1, 0, 0};
    std::vector<int> sandwiches = {0, 1, 0, 1};
    int expected_output = 0;
    int output = sol.countStudents(students, sandwiches);
    
    assert((expected_output == output) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
